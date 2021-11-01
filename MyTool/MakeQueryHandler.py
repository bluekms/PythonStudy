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
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;

namespace NK.LobbyWebAPI.Feature.{name}
{{
    public sealed record Select{name}ListQuery(long Usn) : IQuery;

    public sealed record User{name}(int {name}Id, int UserValue, bool IsReceived);

    public class Select{name}ListQueryHandler : IQueryHandler<Select{name}ListQuery, List<User{name}>>
    {{
        private readonly IMapper mapper;
        private readonly UserService userService;

        public Select{name}ListQueryHandler(UserService userService, IMapper mapper)
        {{
            this.mapper = mapper;
            this.userService = userService;
        }}

        public async Task<List<User{name}>> QueryAsync(Select{name}ListQuery query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var rows = await user.DbContext.User{name}
                .Where(row => row.usn == query.Usn)
                .ToListAsync(cancellationToken);

            return mapper.Map<List<User{name}>>(rows);
        }}
    }}

    internal sealed class {name}Register : IRegister
    {{
        public void Register(TypeAdapterConfig config)
        {{
            config
                .NewConfig<UserDbContext.DBUser{name}, User{name}>()
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
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;
using NK.StaticData;

namespace NK.LobbyWebAPI.Feature.{name}
{{
    public sealed record Exist{name}Query(long Usn, int {name}Id) : IQuery;

    public class Exist{name}QueryHandler : IQueryHandler<Exist{name}Query, bool>
    {{
        private readonly UserService userService;

        public Exist{name}QueryHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task<bool> QueryAsync(Exist{name}Query query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var row = await user.DbContext.User{name}
                    .Where(row => row.usn == query.Usn)
                    .Where(row => row.emergency_quest_id == query.{name}Id)
                    .SingleOrDefaultAsync(cancellationToken);

            return row != null;
        }}
    }}
}}
"""

# ==================================================
#   Main
#   Set Arguments
#       select_row (x)
#       select_rows
#       exist_row
# ==================================================
query = select_rows
name = ""
ret_type = ""

f = open(output_file_name, "w")
f.write(query.format(name=name, ret_type=ret_type))
f.close()
