# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/RuleChecker.cs"

rule_checker = """using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Rule;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record {name}Rule(long Usn, int {feature}Id) : IRule;

    public class {name}RuleChecker : IRuleChecker<{name}Rule>
    {{
        private readonly UserService userService;

        public {name}RuleChecker(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task CheckAsync({name}Rule rule, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(rule.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}", out var resultCode);

            var row = await user.DbContext.User{feature}
                .Where(row => row.usn == rule.Usn)
                .Where(row => row.emergency_quest_id == rule.{feature}Id)
                .SingleOrDefaultAsync(cancellationToken);

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.Failure_{feature}_Not_Exist_Quest);
            }}
        }}
    }}
}}
"""

# ==================================================
#   Main
# ==================================================
query = rule_checker
name = "TouchEmergencyQuestNpc"
feature = "EmergencyQuest"

f = open(output_file_name, "w")
f.write(query.format(name=name, feature=feature))
f.close()
