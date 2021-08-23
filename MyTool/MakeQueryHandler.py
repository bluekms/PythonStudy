# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/QueryHandler.cs"

select_row = """using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Queries
{{
    public sealed record Select{table_name}RowQuery(PacketActionAttribute.PacketCategory PacketCategory, long Usn) : IQuery;

    public class Select{table_name}RowQueryHandler : IQueryHandler<Select{table_name}RowQuery, UserDbContext.DBUser{table_name}>
    {{
        private readonly UserService userService;

        public Select{table_name}RowQueryHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task<UserDbContext.DBUser{table_name}> QueryAsync(Select{table_name}RowQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode, ContentsOpen.None,
                query.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var row = await user.DbContext.User{table_name}
                .Where(row => row.usn == query.Usn)
                .FirstOrDefaultAsync(cancellationToken);

            if (row == null)
            {{
                throw new WebAPIException(ResultCode.Failure_{table_name}_Not_Exist_UserData, $"resultCode: {{resultCode}}");
            }}

            return row;
        }}
    }}
}}

"""

select_rows = """using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Queries
{{
    public sealed record Select{table_name}RowsQuery(PacketActionAttribute.PacketCategory PacketCategory, long Usn) : IQuery;

    public class Select{table_name}RowsQueryHandler : IQueryHandler<Select{table_name}RowsQuery, List<UserDbContext.DBUser{table_name}>>
    {{
        private readonly UserService userService;

        public Select{table_name}RowsQueryHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task<List<UserDbContext.DBUser{table_name}>> QueryAsync(Select{table_name}RowsQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode, ContentsOpen.None,
                query.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var rows = user.DbContext.User{table_name}
                .Where(row => row.usn == query.Usn);

            return await rows.ToListAsync(cancellationToken);
        }}
    }}
}}

"""

select_netlist = """using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using NK.Db;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;
using NK.StaticData;

namespace NK.LobbyWebAPI.Queries
{{
    public sealed record Select{table_name}RowsQuery(PacketActionAttribute.PacketCategory PacketCategory, long Usn) : IQuery;

    public class Select{table_name}NetDataQueryHandler : IQueryHandler<Select{table_name}RowsQuery, List<NetUser{table_name}Data>>
    {{
        private readonly UserService userService;

        public Select{table_name}NetDataQueryHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task<List<NetUser{table_name}Data>> QueryAsync(Select{table_name}RowsQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode, ContentsOpen.None,
                query.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var rows = user.DbContext.User{table_name}
                .Where(row => row.usn == query.Usn);

            var netData = new List<NetUser{table_name}Data>(rows.Count());
            rows.IQueryableToList(netData);

            return netData;
        }}
    }}
}}

"""

# ==================================================
#   Main
#   Set Arguments
#       select_row
#       select_rows
#       select_netlist
# ==================================================
query = select_netlist
table_name = "Reddot"

f = open(output_file_name, "w")
f.write(query.format(table_name = table_name))
f.close()