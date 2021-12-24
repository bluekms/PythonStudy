# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

insert_row = """using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record Insert{name}Command(
        long Usn,
        int {name}Id) : ICommand;

    public class Insert{name}Handler : ICommandHandler<Insert{name}Command>
    {{
        private readonly UserService userService;

        public Insert{name}Handler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Insert{name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var static = DataManager.Instance.Get{name}Table().Find(command.{name}Id);
            
            await user.DbContext.{name}.AddAsync(new()
            {{
                Usn = command.Usn,
                {name}Id = command.{name}Id,
            }});

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}
"""

delete_row = """using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record Delete{name}Command(
        long Usn,
        int {name}Id) : ICommand;

    public class Delete{name}Handler : ICommandHandler<Delete{name}Command>
    {{
        private readonly UserService userService;

        public Delete{name}Handler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Delete{name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var static = DataManager.Instance.Get{name}Table().Find(command.{name}Id);
            if (static == null)
            {{
                throw new WebAPIException(ResultCode.Failure_StaticData_Not_Exist_{name});
            }}

            var row = await user.DbContext.User{name}
                .Where(row => row.usn == command.Usn)
                .Where(row => row.{name}__id == command.{name}Id)
                .SingleOrDefaultAsync();

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.Failure_{name}_Not_Exist_);
            }}

            user.DbContext.User{name}.Remove(row);

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}
"""

update_row_void = """using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record Update{name}{target_name}Command(
        long Usn,
        int {name}Id) : ICommand;

    public class Update{name}{target_name}Handler : ICommandHandler<Update{name}{target_name}Command>
    {{
        private readonly UserService userService;

        public Update{name}{target_name}Handler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Update{name}{target_name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var row = await user.DbContext.User{name}
                .Where(row => row.Usn == command.Usn)
                .Where(row => row.emergency_id == command.{name}Id)
                .SingleOrDefaultAsync();

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.FailureDbUserNotExistUsn);
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
#       delete_row
#       update_row_void (new)
# ==================================================
query = insert_row
feature = "Trigger2"
name = "Rewarded"
target_name = ""

f = open(output_file_name, "w")
f.write(query.format(name=name, target_name=target_name, feature=feature))
f.close()
