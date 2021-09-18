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

update_row_void = """using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Update{name}{target_name}Command(
        long Usn,
        int {name}Id) : ICommand;

    public class Update{name}{target_name}CommandHandler : ICommandHandler<Update{name}{target_name}Command>
    {{
        private readonly UserService userService;

        public Update{name}{target_name}CommandHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Update{name}{target_name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}", out var resultCode, ContentsOpen.{name});
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var row = await user.DbContext.User{name}
                .Where(row => row.usn == command.Usn)
                .Where(row => row.emergency_quest_id == command.{name}Id)
                .SingleOrDefaultAsync();

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.Failure_{name}_Not_Exist_Quest);
            }}

            // TODO

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}
"""

# ==================================================
#   Main
#   Set Arguments
#       insert_row (new)
#       delete_row (new)
#       update_row_void (new)
# ==================================================
query = update_row_void
name = "EmergencyQuest"
target_name = "IsReceived"

f = open(output_file_name, "w")
f.write(query.format(name=name, target_name=target_name))
f.close()
