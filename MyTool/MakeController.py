# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

void_controller = """using System;
using System.Threading;
using System.Threading.Tasks;
using MapsterMapper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Feature.Common;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    public class {name}Controller : Controller
    {{
        private sealed record RequestWrapper(long Usn);

        private sealed record ResponseWrapper(NetCommonData CommonData);

        private readonly ILogger<{name}Controller> logger;
        private readonly IMapper mapper;
        private readonly UserService userService;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Controller(
            ILogger<{name}Controller> logger,
            IMapper mapper,
            UserService userService,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.mapper = mapper;
            this.userService = userService;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/{name_lower}/get")]
        public async Task<Res{name}> {name}(
            [FromBody] Req{name} request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.usn), cancellationToken);
                if (res == null)
                {{
                    return new Res{name}
                    {{
                        result = ResultCode.Failure_SystemError,
                    }};
                }}

                return new Res{name}
                {{
                    result = ResultCode.Success,
                    CommonData = res.CommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{name} failed. ResultCode : {{resultcode}}", webApiException.ResultCode);
                return new Res{name}
                {{
                    result = webApiException.ResultCode,
                }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{name} failed.");
                return new Res{name}
                {{
                    result = ResultCode.Failure_SystemError,
                }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            var commonData = await getCommonData.QueryAsync(new(request.Usn), cancellationToken);

            return new(commonData);
        }}
    }}
}}
"""

list_controller = """using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    [ApiController]
    public class Get{name}Contrller : Controller
    {{
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn);

        private sealed record ResponseWrapper(List<int> {name}s, NetCommonData NetCommonData);

        private readonly ILogger<{name}Contrller> logger;
        private readonly UserService userService;
        private readonly IQueryHandler<Select{name}Query, List<int>> select{name}Query;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public Get{name}Contrller(
            ILogger<{name}Contrller> logger,
            UserService userService,
            IQueryHandler<Select{name}Query, List<int>> select{name}Query,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.userService = userService;
            this.select{name}RowsQuery = select{name}RowsQuery;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/{name}/get")]
        public async Task<ResGet{name}> Get{name}(
            [FromBody] ReqGet{name} request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.PacketCategory, request.usn), cancellationToken);
                if (res == null)
                {{
                    return new ResGet{name} {{ result = ResultCode.Failure_SystemError }};
                }}

                return new ResGet{name}()
                {{
                    result = ResultCode.Success,
                    costume_ids = {{ res.{name}s }},
                    CommonData = res.NetCommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{Name} failed. {ResultCode}", MethodBase.GetCurrentMethod().Name, webApiException.ResultCode);
                return new ResGet{name} {{ result = webApiException.ResultCode }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{name} failed.");
                return new ResGet{name} {{ result = ResultCode.Failure_SystemError }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            var list = await select{name}RowsQuery.QueryAsync(new(request.PacketCategory, request.Usn));

            var commonData = await getCommonData.QueryAsync(new(request.PacketCategory, request.Usn), cancellationToken);

            return new(list, commonData);
        }}
    }}
}}


"""

currency_controller = """using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    [ApiController]
    public class {name}Contrller : Controller
    {{
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn, int CostumeId);

        private sealed record ResponseWrapper(List<NetCurrencyData> NetCurrencyData, NetCommonData NetCommonData);

        private readonly ILogger<{name}Contrller> logger;
        private readonly UserService userService;
        private readonly ICommandHandler<{name}Command> insertCharacterCostumeCommand;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Contrller(
            ILogger<{name}Contrller> logger,
            UserService userService,
            ICommandHandler<{name}Command> insertCharacterCostumeCommand,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.userService = userService;
            this.insertCharacterCostumeCommand = insertCharacterCostumeCommand;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/character/costume/buy")]
        public async Task<Res{name}> {name}(
            [FromBody] Req{name} request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.PacketCategory, request.usn, request.costume_id), cancellationToken);
                if(res == null)
                {{
                    return new Res{name} {{ result = ResultCode.Failure_SystemError }};
                }}

                return new Res{name}()
                {{
                    result = ResultCode.Success,
                    currencies = {{ res.NetCurrencyData }},
                    CommonData = res.NetCommonData
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{Name} failed. {ResultCode}", MethodBase.GetCurrentMethod().Name, webApiException.ResultCode);
                return new Res{name} {{ result = webApiException.ResultCode }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{name} failed.");
                return new Res{name} {{ result = ResultCode.Failure_SystemError }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            await insertCharacterCostumeCommand.ExecuteAsync(new(request.PacketCategory, request.Usn, request.CostumeId));

            var commonData = await getCommonData.QueryAsync(new(request.PacketCategory, request.Usn), cancellationToken);

            return new(commonData);
        }}
    }}
}}

"""

# ==================================================
#   Main
#   Set Arguments
#       void_controller (Update)
#       list_controller
#       currency_controller
# ==================================================
query = void_controller
name = "ListMail"

f = open(output_file_name, "w")
f.write(query.format(name=name, name_lower=name.lower()))
f.close()
