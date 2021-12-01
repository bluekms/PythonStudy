# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/Rule.cs"

rule = """using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Rule;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using IRule = Microsoft.AspNetCore.Rewrite.IRule;

namespace NK.LobbyWebAPI.Feature.EmergencyQuest
{{
    public sealed record {name}Rule(long Usn) : IRule;

    public class {name}RuleChecker : IRuleChecker<{name}Rule>
    {{
        private readonly UserService userService;

        public {name}RuleChecker(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task CheckAsync({name}Rule rule, CancellationToken cancellationToken)
        {{
            using var user = userService.UserManager.LoadUser(rule.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}", out var resultCode);
            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}
        }}
    }}
}}
"""

# ==================================================
#   Main
#   Set Arguments
# ==================================================
query = rule
_name = "CancleEmergencyQuest"

f = open(output_file_name, "w")
f.write(query.format(name=_name))
f.close()
