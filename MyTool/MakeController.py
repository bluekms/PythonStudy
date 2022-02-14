# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

void_controller = """using System;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using MapsterMapper;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Authorization;
using NK.LobbyWebAPI.Queries;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.{feature}
{{
    [ApiController]
    [Authorize(NKPolicy.TokenWithSessionKey)]
    public class {_name}Controller : ControllerBase
    {{
        private readonly ILogger logger;
        private readonly IMapper mapper;

        public {_name}Controller(
            ILogger<{_name}Controller> logger,
            IMapper mapper)
        {{
            this.logger = logger;
            this.mapper = mapper;
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

                return mapper.Map<Res{_name}>(res);
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "{{name}} failed. Request: {{@Request}}", MethodBase.GetCurrentMethod()?.Name, request);
                return new Res{_name}
                {{
                    Result = webApiException.ResultCode,
                }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "{{name}} failed. Request: {{@Request}}", MethodBase.GetCurrentMethod()?.Name, request);
                return new Res{_name}
                {{
                    Result = ResultCode.FailureSystemError,
                }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            return new(ResultCode.Success);
        }}
        
        private sealed record RequestWrapper(long Usn);

        private sealed record ResponseWrapper(ResultCode Result);
    }}
}}
"""

# ==================================================
#   Main
#   Set Arguments
#       void_controller
# ==================================================
query = void_controller
feature = "Messenger"
_name = "FinSubQuest"

f = open(output_file_name, "w")
f.write(query.format(_name=_name, name_lower=_name.lower(), feature=feature))
f.close()
