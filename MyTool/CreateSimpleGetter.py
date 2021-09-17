# ==================================================
#   Detail
# ==================================================
controller_file_name = "./MyTool/build/Controller.cs"
queryhandler_file_name = "./MyTool/build/QueryHandler.cs"

controller = """using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using MapsterMapper;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Feature.Common;
using NK.LobbyWebAPI.Feature.{name};
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    public class Get{name}DataController : Controller
    {{
        private sealed record RequestWrapper(long Usn);

        private sealed record ResponseWrapper(List<User{name}> {name}List, NetCommonData CommonData);

        private readonly ILogger<Get{name}DataController> logger;
        private readonly IMapper mapper;
        private readonly IQueryHandler<Select{name}ListQuery, List<User{name}>> selectEmergencyQueryList;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public Get{name}DataController(
            ILogger<Get{name}DataController> logger,
            IMapper mapper,
            IQueryHandler<Select{name}ListQuery, List<User{name}>> selectEmergencyQueryList,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.mapper = mapper;
            this.selectEmergencyQueryList = selectEmergencyQueryList;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/{name_lower}/get")]
        public async Task<ResGet{name}Data> Get{name}Data(
            [FromBody] ReqGet{name}Data request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.usn), cancellationToken);
                if (res == null)
                {{
                    return new ResGet{name}Data
                    {{
                        result = ResultCode.Failure_SystemError,
                    }};
                }}

                return new ResGet{name}Data
                {
                    result = ResultCode.Success,
                    CommonData = res.CommonData,
                };
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "Get{name}Data failed. ResultCode : {{resultcode}}", webApiException.ResultCode);
                return new ResGet{name}Data
                {{
                    result = webApiException.ResultCode,
                }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "Get{name}Data failed.");
                return new ResGet{name}Data
                {{
                    result = ResultCode.Failure_SystemError,
                }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            var list = await selectEmergencyQueryList.QueryAsync(new(request.Usn), cancellationToken);
            var commonData = await getCommonData.QueryAsync(new(request.Usn), cancellationToken);

            return new(list, commonData);
        }}
    }}
}}
"""

query_handler = """using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Mapster;
using MapsterMapper;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;

namespace NK.LobbyWebAPI.Feature.{name}
{{
    public sealed record Select{name}ListQuery(long Usn) : IQuery;

    public sealed record User{name}(int {name}Id);

    public class Select{name}ListQueryHandler : IQueryHandler<Select{name}ListQuery, List<User{name}>>
    {{
        private readonly IMapper mapper;
        private readonly UserService userService;

        public Select{name}ListQueryHandler(UserService userService, IMapper mapper)
        {{
            this.userService = userService;
            this.mapper = mapper;
        }}

        public async Task<List<User{name}>> QueryAsync(Select{name}ListQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var rows = await user.DbContext.User{name}
                .Where(row => row.usn == query.Usn)
                .ToListAsync(cancellationToken);

            return mapper.Map<List<User{name}>>(rows);
        }}
    }}

    internal sealed class {name}Register : IRegister
    {{
        public void Register(TypeAdapterConfig config)
        {{
            config
                .NewConfig<UserDbContext.DBUser{name}, User{name}>()
                .MapToConstructor(true);
        }}
    }}
}}
"""

# ==================================================
#   Main
# ==================================================
name = "EmergencyQuest"

f = open(controller_file_name, "w")
f.write(controller.format(name=name, name_lower=name.lower()))
f.close()

f = open(queryhandler_file_name, "w")
f.write(query_handler.format(name=name))
f.close()
