# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

default = """using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.LobbyWebAPI.Feature.Common;
using NK.LobbyWebAPI.Queries;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    public class {name}Controller : Controller
    {{
        private sealed record RequestWrapper(long Usn, int {name}Id);

        private sealed record ResponseWrapper(NetCommonData CommonData);

        private readonly ILogger<{name}Controller> logger;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Controller(
            ILogger<{name}Controller> logger,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/{name_lower}")]
        public async Task<Res{name}> {name}(
            [FromBody] Req{name} request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.usn, request.emergency_quest_id), cancellationToken);
                if (res == null)
                {{
                    return new Res{name}
                    {{
                        result = ResultCode.Failure_SystemError,
                    }};
                }}

                return new Res{name}
                {{
                    result = ResultCode.Failure_SystemError,
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

# ==================================================
#   Main
#       defauilt
# ==================================================
query = default
name = "CancelEmergencyQuest"

f = open(output_file_name, "w")
f.write(query.format(name=name, name_lower=name.lower()))
f.close()
