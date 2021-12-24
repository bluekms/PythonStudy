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
using MapsterMapper;
using Microsoft.EntityFrameworkCore;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record {name}Query(long Usn) : IQuery;

    public sealed record {ret_type}(int {name}Id, int UserValue, bool IsReceived);

    public class {name}Handler : IQueryHandler<{name}Query, List<{ret_type}>>
    {{
        private readonly IMapper mapper;
        private readonly UserService userService;

        public {name}Handler(UserService userService, IMapper mapper)
        {{
            this.mapper = mapper;
            this.userService = userService;
        }}

        public async Task<List<{ret_type}>> QueryAsync({name}Query query, CancellationToken cancellationToken = default)
        {{
            using var user = userService.UserManager.LoadUser(query.Usn, true,
                $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod()?.Name}}", out var resultCode);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode);
            }}

            var rows = await user.DbContext.{name}
                .Where(row => row.Usn == query.Usn)
                .ToListAsync(cancellationToken);
                // .FindAsync(new object[] {{ query.Usn, query.{name}Id }}, cancellationToken);

            return mapper.Map<List<{ret_type}>>(rows);
        }}
    }}

    internal sealed class {ret_type}Register : IRegister
    {{
        public void Register(TypeAdapterConfig config)
        {{
            config
                .NewConfig<UserDbContext.DBUser{name}, {ret_type}>()
                .MapToConstructor(true);
        }}
    }}
}}
"""

exist_row = """using System.Reflection;
using System.Threading;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Services;
using NK.Network.Packet;

namespace NK.LobbyWebAPI.Feature.{feature}
{{
    public sealed record Exist{name}Query(
        long Usn,
        int {name}Id) : IQuery;

    public class Exist{name}Handler : IQueryHandler<Exist{name}Query, bool>
    {{
        private readonly UserService userService;

        public Exist{name}Handler(UserService userService)
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
                .FindAsync(new object[] {{ query.Usn, query.{name}Id }}, cancellationToken);

            return row != null;
        }}
    }}
}}
"""

# ==================================================
#   Main
#   Set Arguments
#       select_rows
#       exist_row
# ==================================================
query = select_rows
feature = "MainQuest"
name = "GetUserMainQuest"
ret_type = "UserMainQuest"

f = open(output_file_name, "w")
f.write(query.format(name=name, ret_type=ret_type, feature=feature))
f.close()
