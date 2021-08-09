# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/CommandHandler.cs"

create_rows = """using System;
using System.Collections.Generic;
using System.Reflection;
using System.Threading.Tasks;
using NK.LobbyWebAPI.Models;
using NK.LobbyWebAPI.Services;
using NK.Network.Data;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;
using NK.StaticData;

namespace NK.LobbyWebAPI.Commands
{{
    public sealed record Create{table_name}Command(
        PacketActionAttribute.PacketCategory PacketCategory,
        long Usn,
        List<Net{table_name}Data> {table_name}s) : ICommand;

    public class Create{table_name}CommandHandler : ICommandHandler<Create{table_name}Command>
    {{
        private readonly UserService userService;

        public Create{table_name}CommandHandler(UserService userService)
        {{
            this.userService = userService;
        }}

        public async Task ExecuteAsync(Create{table_name}Command command)
        {{
            using var user = userService.UserManager.LoadUser(command.Usn, true, $"{{GetType().Name}}.{{MethodBase.GetCurrentMethod().Name}}",
                out var resultCode, ContentsOpen.None, command.PacketCategory);

            if (resultCode != ResultCode.Success)
            {{
                throw new WebAPIException(resultCode, $"LoadUser failed, resultCode : {{resultCode}}");
            }}

            var rand = new Random();
            foreach (var {table_name} in command.{table_name}s)
            {{
                var row = new UserDbContext.DBUser{table_name}()
                {{
                    usn = command.Usn,
                    {table_name}_key = rand.Next(short.MinValue, short.MaxValue),
                    content_type = ({table_name}ContentType){table_name}.content_type,
                    {table_name}_data = string.Empty
                }};

                user.DbContext.User{table_name}.Add(row);
            }}

            await user.DbContext.SaveChangesAsync();
        }}
    }}
}}

"""

# ==================================================
#   Main
#   Set Arguments
#       create_rows
# ==================================================
query = create_rows
table_name = "Reddot"

f = open(output_file_name, "w")
f.write(query.format(table_name = table_name))
f.close()
