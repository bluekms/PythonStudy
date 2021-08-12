# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

controller = """using System;
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
        private sealed record RequestWrapper(PacketActionAttribute.PacketCategory PacketCategory, long Usn, List<int> Data);

        private sealed record ResponseWrapper(NetCommonData NetCommonData);

        private readonly UserService userService;
        private readonly ICommandHandler<{name}Command> {name}Command;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public {name}Contrller(
            UserService userService,
            ICommandHandler<{name}Command> {name}Command,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.userService = userService;
            this.{name}Command = {name}Command;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/user/req{name}data")]
        public async Task<Res{name}Data> {name}Data(
            [FromBody] Req{name}Data request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                await HandleAsync(new(request.PacketCategory, request.usn, request.reddot_keys.ToList()), cancellationToken);

                return new Res{name}Data()
                {{
                    result = ResultCode.Success
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                NKLog.LogError($"{name}Data failed. resultcode: {{webApiException.ResultCode}}, Message: {{webApiException.Message}},  usn: {{request.usn}}");
                return new Res{name}Data {{ result = webApiException.ResultCode }};
            }}
            catch (Exception e)
            {{
                NKLog.LogError($"{name}Data failed. Message: {{e.Message}}, usn: {{request.usn}}");
                return new Res{name}Data {{ result = ResultCode.Failure_SystemError }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            await {name}Command.ExecuteAsync(new(request.PacketCategory, request.Usn, request.Data));

            var commonData = await getCommonData.QueryAsync(new(request.PacketCategory, request.Usn), cancellationToken);

            return new(commonData);
        }}
    }}
}}
 
"""

# ==================================================
#   Main
#   Set Arguments
#       controller
# ==================================================
query = controller
name = "CreateReddot"

f = open(output_file_name, "w")
f.write(query.format(name = name))
f.close()