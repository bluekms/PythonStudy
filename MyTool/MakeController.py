# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

void_controller = """using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Controllers.v1.Character;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    [ApiController]
    public class {name}Contrller : ControllerBase
    {{
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn);

        private sealed record ResponseWrapper(NetCommonData NetCommonData);

        private readonly UserService userService;
        private readonly ILogger<CharacterLevelUpController> logger;
        private readonly ICommandHandler<UpdateUserDataCostumeLvCommand> {name}Command;
        private readonly ICommandHandler<UpdateUserDataCostumeLvCommand, int> updateUserDataCostumeLv;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Contrller(
            UserService userService,
            ILogger<CharacterLevelUpController> logger,
            ICommandHandler<UpdateUserDataCostumeLvCommand> {name}Command,
            ICommandHandler<UpdateUserDataCostumeLvCommand, int> updateUserDataCostumeLv,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.userService = userService;
            this.logger = logger;
            this.{name}Command = {name}Command;
            this.updateUserDataCostumeLv = updateUserDataCostumeLv;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/character/costume/levelup")]
        public async Task<Res{name}e> {name}(
            [FromBody] Req{name}e request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.PacketCategory, request.usn), cancellationToken);

                return new Res{name}e()
                {{
                    result = ResultCode.Success,
                    CommonData = res.NetCommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{name} failed. Request: {{@request}}", request);
                return new Res{name}e {{ result = webApiException.ResultCode }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{name} failed. Raised Exception.");
                return new Res{name}e {{ result = ResultCode.Failure_SystemError }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            await {name}Command.ExecuteAsync(new(request.PacketCategory, request.Usn));

            var commonData = await getCommonData.QueryAsync(new(request.PacketCategory, request.Usn), cancellationToken);

            return new(commonData);
        }}
    }}
}}

"""

list_controller = """using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Log;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    [ApiController]
    public class Get{name}Contrller : Controller
    {{
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn);

        private sealed record ResponseWrapper(List<int> {name}s, NetCommonData NetCommonData);

        private readonly UserService userService;
        private readonly IQueryHandler<Select{name}RowsQuery, List<int>> select{name}RowsQuery;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public Get{name}Contrller(
            UserService userService,
            IQueryHandler<Select{name}RowsQuery, List<int>> select{name}RowsQuery,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.userService = userService;
            this.select{name}RowsQuery = select{name}RowsQuery;
            this.getCommonData = getCommonData;
        }}

        [HttpPost(/* TODO */"v1/character/costume/get")]
        public async Task<ResGet{name}Data> Get{name}Data(
            [FromBody] ReqGet{name}Data request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.PacketCategory, request.usn), cancellationToken);
                if (res == null)
                {{
                    return new ResGet{name}Data {{ result = ResultCode.Failure_SystemError }};
                }}

                return new ResGet{name}Data()
                {{
                    result = ResultCode.Success,
                    costume_ids = {{ res.{name}s }},
                    CommonData = res.NetCommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                NKLog.LogError($"Get{name}Data failed. resultcode: {{webApiException.ResultCode}}, Message: {{webApiException.Message}},  usn: {{request.usn}}");
                return new ResGet{name}Data {{ result = webApiException.ResultCode }};
            }}
            catch (Exception e)
            {{
                NKLog.LogError($"Get{name}Data failed. Message: {{e.Message}}, usn: {{request.usn}}");
                return new ResGet{name}Data {{ result = ResultCode.Failure_SystemError }};
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
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Log;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    [ApiController]
    public class {name}Contrller : Controller
    {{
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn, int CostumeId);

        private sealed record ResponseWrapper(List<NetCurrencyData> NetCurrencyData, NetCommonData NetCommonData);

        private readonly UserService userService;
        private readonly ICommandHandler<{name}Command> insertCharacterCostumeCommand;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Contrller(
            UserService userService,
            ICommandHandler<{name}Command> insertCharacterCostumeCommand,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
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
                NKLog.LogError($"{name}Data failed. resultcode: {{webApiException.ResultCode}}, Message: {{webApiException.Message}},  usn: {{request.usn}}");
                return new Res{name} {{ result = webApiException.ResultCode }};
            }}
            catch (Exception e)
            {{
                NKLog.LogError($"{name}Data failed. Message: {{e.Message}}, usn: {{request.usn}}");
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
#       void_controller
#       list_controller
#       currency_controller
# ==================================================
query = void_controller
name = "LevelUpCharacterCostum"

f = open(output_file_name, "w")
f.write(query.format(name = name))
f.close()
