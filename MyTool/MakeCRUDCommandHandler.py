# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

insert_row = """using System.Reflection;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Insert{name}Command(
        long Usn,
        int {name}Id) : ICommand;

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

            var staticQuest = DataManager.Instance.Get{name}Table().Find(command.{name}Id);
            if (staticQuest == null)
            {{
                throw new WebAPIException(ResultCode.Failure_StaticData_Not_Exist_{name});
            }}

            user.DbContext.User{name}.Add(new UserDbContext.DBUser{name}
            {{
                usn = command.Usn,
                user_value = 0,
                clear_value = staticQuest.Clear_condition_value,
                is_received = false,
            }});

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}
"""

delete_row = """using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Delete{name}QuestCommand(
        long Usn,
        int {name}QuestId) : ICommand;

    public class Delete{name}QuestCommandHandler : ICommandHandler<Delete{name}QuestCommand>
    {{
        private readonly UserService userService;

        public Delete{name}QuestCommandHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Delete{name}QuestCommand command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var staticQuest = DataManager.Instance.Get{name}QuestTable().Find(command.{name}QuestId);
            if (staticQuest == null)
            {{
                throw new WebAPIException(ResultCode.Failure_StaticData_Not_Exist_{name}Quest);
            }}

            var row = user.DbContext.User{name}Quest
                .Where(row => row.usn == command.Usn)
                .Where(row => row.{name}_quest_id == command.{name}QuestId)
                .SingleOrDefault();

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.Failure_{name}Quest_Not_Exist_Quest);
            }}

            user.DbContext.User{name}Quest.Remove(row);

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
#       insert_row (new)
#       delete_row (new)
#       update_row_int
# ==================================================
query = delete_row
table_name = "EmergencyQuest"

f = open(output_file_name, "w")
f.write(query.format(table_name=table_name))
f.close()
