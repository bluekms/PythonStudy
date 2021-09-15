# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

insert_rows = """using System;
using System.Collections.Generic;
using System.Reflection;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Data;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Insert{name}Command(
        long Usn,
        Net{name} {name}) : ICommand;

    public class Insert{name}CommandHandler : ICommandHandler<Insert{name}Command>
    {{
        private readonly UserService userService;

        public Insert{name}CommandHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Insert{name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var row = new UserDbContext.DBUser{name}
            {{
                usn = command.Usn,
            }};

            user.DbContext.User{name}.Add(row);

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}
"""

update_row_int = """using System.Collections.Generic;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Update{table_name}Command(
        PacketActionAttribute.PacketCategory PacketCategory,
        long Usn) : ICommand;

    public class Update{table_name}CommandHandler : ICommandHandler<Update{table_name}Command, int>
    {{
        private readonly UserService userService;
        private readonly IQueryHandler<SelectCharacterCostumeRowsQuery, List<int>> selectCharacterCostume;

        public Update{table_name}CommandHandler(UserService userService, IQueryHandler<SelectCharacterCostumeRowsQuery, List<int>> selectCharacterCostume)
        {{
            this.userService = userService;
            this.selectCharacterCostume = selectCharacterCostume;
        }}

        public async Task<int> ExecuteAsync(Update{table_name}Command command, CancellationToken cancellationToken)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}",
                out var resultCode, ContentsOpen.None, command.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            // TODO

            await user.DbContext.SaveChangesAsync();

            return nextLv;
        }}
    }}
}}

"""

# ==================================================
#   Main
#   Set Arguments
#       insert_rows
#       update_row_int
# ==================================================
query = insert_rows
table_name = "EmergencyQuest"

f = open(output_file_name, "w")
f.write(query.format(table_name=table_name))
f.close()
