# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/QueryHandler.cs"

select_row = """
"""

select_rows = """using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Mapster;
using MapsterMapper;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Data;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Queries
{{
    public sealed record SelectReddotQuery(PacketActionAttribute.PacketCategory PacketCategory, long Usn, long seq) : IQuery;

    public sealed record User{name}(long Seq, ReddotContentType ContentType, string ReddotData);

    public class SelectReddotQueryHandler : IQueryHandler<SelectReddotQuery, List<{name}>>
    {{
        private readonly UserService userService;
        private readonly IMapper mapper;

        public SelectReddotQueryHandler(UserService userService, IMapper mapper)
        {{
            this.userService = userService;
            this.mapper = mapper;
        }}

        public async Task<List<{name}>> QueryAsync(SelectReddotQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode, ContentsOpen.None,
                query.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            return await Task.Run(() =>
            {{
                var rows = user.DbContext.User{name}
                    .Where(row => query.seq <= row.seq)
                    .Where(row => query.Usn == row.usn);

                var {name}s = mapper.Map<List<{name}>>(rows);

                return {name}s;
            }});
        }}
    }}

    internal sealed class {name}Register : IRegister
    {{
        public void Register(TypeAdapterConfig config)
        {{
            config
                .NewConfig<UserDbContext.DB{name}, {name}>()
                .MapToConstructor(true);
        }}
    }}
}}
"""

exist_row = """using System.Linq;
using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Queries
{{
    public sealed record Exist{name}Query(PacketActionAttribute.PacketCategory PacketCategory, long Usn, long seq) : IQuery;

    public class Exist{name}QueryHandler : IQueryHandler<Select{name}Query, bool>
    {{
        private readonly UserService userService;

        public Exist{name}QueryHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task<bool> QueryAsync(Select{name}Query query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode, ContentsOpen.None,
                query.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            return await Task.Run(() =>
            {{
                var rows = user.DbContext.User{name}
                    .Where(row => query.seq <= row.seq)
                    .Where(row => query.Usn == row.usn)
                    .FirstOrDefaultAsync(cancellationToken);

                return rows != null;
            }});
        }}
    }}
}}

"""

# ==================================================
#   Main
#   Set Arguments
#       select_row
#       select_rows
#       exist_row
# ==================================================
query = exist_row
name = "Reddot"
ret_type = ""

f = open(output_file_name, "w")
f.write(query.format(name = name, ret_type = ret_type))
f.close()