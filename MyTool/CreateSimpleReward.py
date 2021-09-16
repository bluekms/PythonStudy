# ==================================================
#   Detail
# ==================================================
controller_file_name = "./MyTool/build/Controller.cs"

controller = """using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using NK.GameData;
using NK.LobbyWebAPI.Commands;
using NK.LobbyWebAPI.Feature.Common;
using NK.LobbyWebAPI.Feature.{name};
using NK.LobbyWebAPI.Feature.Reward;
using NK.LobbyWebAPI.Queries;
using NK.LobbyWebAPI.Rule;
using NK.Network.Packet;
using NK.Network.Packet.Lobby;
using NK.StaticData;

namespace NK.LobbyWebAPI.Controllers.v1
{{
    public class Obtain{name}RewardController : Controller
    {{
        private sealed record RequestWrapper(long Usn, int {name}Id);

        private sealed record ResponseWrapper(NetRewardData Reward, NetCommonData CommonData);

        private readonly ILogger<Obtain{name}RewardController> logger;
        private readonly IRuleChecker<Obtain{name}Rule> obtain{name}Rule;
        private readonly IQueryHandler<Get{name}StaticDataQuery, {name}Record> get{name}StaticData;
        private readonly ICommandHandler<RewardCommand, InternalRewardData> reward;
        private readonly IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData;

        public Obtain{name}RewardController(
            ILogger<Obtain{name}RewardController> logger,
            IRuleChecker<Obtain{name}Rule> obtain{name}Rule,
            IQueryHandler<Get{name}StaticDataQuery, {name}Record> get{name}StaticData,
            ICommandHandler<RewardCommand, InternalRewardData> reward,
            IQueryHandler<GetCommonDataQuery, NetCommonData> getCommonData)
        {{
            this.logger = logger;
            this.obtain{name}Rule = obtain{name}Rule;
            this.get{name}StaticData = get{name}StaticData;
            this.reward = reward;
            this.getCommonData = getCommonData;
        }}

        [HttpPost("v1/{name_lower}/reward")]
        public async Task<ResObtain{name}Reward> Obtain{name}Reward(
            [FromBody] ReqObtain{name}Reward request,
            CancellationToken cancellationToken)
        {{
            try
            {{
                var res = await HandleAsync(new(request.usn, request.emergency_quest_id), cancellationToken);
                if (res == null)
                {{
                    return new ResObtain{name}Reward
                    {{
                        result = ResultCode.Failure_SystemError,
                    }};
                }}

                return new ResObtain{name}Reward
                {{
                    result = ResultCode.Failure_SystemError,
                    reward = res.Reward,
                    CommonData = res.CommonData,
                }};
            }}
            catch (WebAPIException webApiException)
            {{
                logger.LogError(webApiException, "Obtain{name}Reward failed. ResultCode : {{resultcode}}", webApiException.ResultCode);
                return new ResObtain{name}Reward
                {{
                    result = webApiException.ResultCode,
                }};
            }}
            catch (Exception ex)
            {{
                logger.LogError(ex, "Obtain{name}Reward failed.");
                return new ResObtain{name}Reward
                {{
                    result = ResultCode.Failure_SystemError,
                }};
            }}
        }}

        private async Task<ResponseWrapper> HandleAsync(RequestWrapper request, CancellationToken cancellationToken)
        {{
            await obtain{name}Rule.CheckAsync(new(request.Usn, request.{name}Id), cancellationToken);

            var static{name} = await get{name}StaticData.QueryAsync(new(request.{name}Id), cancellationToken);
            var rewardData = new InternalRewardData(UpdateEventType.{name}Reward);
            if (static{name}.Reward_id != 0)
            {{
                rewardData = await reward.ExecuteAsync(new(request.Usn, static{name}.Reward_id, 0, UpdateEventType.{name}Reward));
            }}

            var commonData = await getCommonData.QueryAsync(new(request.Usn), cancellationToken);

            return new(null, commonData);
        }}
    }}
}}

"""

# ==================================================
#   Main
# ==================================================
name = "EmergencyQuest"

f = open(controller_file_name, "w")
f.write(controller.format(name=name, name_lower=name.lower()))
f.close()
