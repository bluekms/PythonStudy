# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Controller.cs"

void_controller = """using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using NK.LobbyWebAPI.Authorization;
using NK.Network.Packet.Lobby;
using ProtobufFormatter;

namespace NK.LobbyWebAPI.Controllers.{feature}
{{
    [ProtobufRequest(typeof(Req{name}))]
    public sealed record Request{name}(
        long Usn);

    [ProtobufResponse(typeof(Res{name}))]
    public sealed record Response{name}();

    [ApiController]
    [Authorize(NKPolicy.TokenWithSessionKey)]
    public class {name}Controller : ControllerBase
    {{
        // TODO
        [HttpPost("v1/")]
        public async Task<Response{name}> {name}([FromBody] Req{name} request)
        {{
            return new();
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
feature = "Cheat.Tutorial"
name = "AllClearTutorial"

f = open(output_file_name, "w")
f.write(query.format(name=name, feature=feature))
f.close()
