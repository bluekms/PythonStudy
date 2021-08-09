# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

delete_row = """
"""

delete_rows = """using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Delete{table_name}Command(PacketActionAttribute.PacketCategory PacketCategory, long Usn, List<int> {table_name}Keys) : ICommand;

    public class Delete{table_name}CommandHandler : ICommandHandler<Delete{table_name}Command>
    {{
        private readonly UserService userService;

        public Delete{table_name}CommandHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Delete{table_name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}",
                out var resultCode, ContentsOpen.None, command.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode, $"LoadUser failed, resultCode : {{resultCode}}");
            }}

            // TODO

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}

"""

delete_all = """
"""

# ==================================================
#   Main
#   Set Arguments
#       delete_row (x)
#       delete_rows
#       delete_all (x)
# ==================================================
query = delete_rows
table_name = "Reddot"

f = open(output_file_name, "w")
f.write(query.format(table_name = table_name))
f.close()