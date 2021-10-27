# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

void_controller = """using System;
using System.Reflection;
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
    [ApiController]
    public class {_name}Controller : Controller
    {{
        private sealed record RequestWrapper(long Usn);

        private sealed record ResponseWrapper(NetCommonData CommonData);

        private readonly ILogger logger;
        private readonly IMapper mapper;
        private readonly UserService userService;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {_name}Controller(
            ILogger logger,
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
        public async Task<Res{_name}> {_name}(
            [FromBody] Req{_name} request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.Usn), cancellationToken);
                if (res == null)
                {{
                    return new Res{_name}
                    {{
                        Result = ResultCode.FailureSystemError,
                    }};
                }}

                return new Res{_name}
                {{
                    Result = ResultCode.Success,
                    CommonData = res.CommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{{name}} failed. Request: {{Request}}", MethodBase.GetCurrentMethod().Name, request);
                return new Res{_name}
                {{
                    Result = webApiException.ResultCode,
                }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{{name}} failed. Request: {{Request}}", MethodBase.GetCurrentMethod()?.Name, request);
                return new Res{_name}
                {{
                    Result = ResultCode.FailureSystemError,
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

# ==================================================
#   Main
#   Set Arguments
#       void_controller
# ==================================================
query = void_controller
_name = "ObtainMessageReward"

f = open(output_file_name, "w")
f.write(query.format(_name=_name, name_lower=_name.lower()))
f.close()
