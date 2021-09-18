# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/StaticDataQueryHandler.cs"

get_staticdata = """using System.Threading;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Queries;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Feature.StaticData
{{
    public sealed record Get{name}StaticDataQuery(int {name}Id) : IQuery;

    public class Get{name}StaticDataQueryHandler : IQueryHandler<Get{name}StaticDataQuery, {name}Record>
    {{
        public async Task<{name}Record> QueryAsync(Get{name}StaticDataQuery query, CancellationToken cancellationToken = default)
        {{
            var staticData = await Task.Run(() => DataManager.Instance.Get{name}Table().Find(query.{name}Id), cancellationToken);
            if (staticData == null)
            {{
                throw new WebAPIException(ResultCode.Failure_StaticData_Not_Exist_{name});
            }}

            return staticData;
        }}
    }}
}}
"""

# ==================================================
#   Main
# ==================================================
query = get_staticdata
name = "EmergencyStage"
ret_type = ""

f = open(output_file_name, "w")
f.write(query.format(name=name, ret_type=ret_type))
f.close()
