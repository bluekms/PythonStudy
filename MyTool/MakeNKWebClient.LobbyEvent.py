# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/NKWebClient.LobbyEvent.cs"

simple_packet = """public async UniTask<Res{name}> Request{name}Async(Action<Res{name}> handler)
{{
    var res = await NetworkManager.Instance.Client.SendAsync<Res{name}>(
        new Req{name}
        {{
            usn = NKUserData.AccountData.USN,
        }});

    if (res.result == ResultCode.Success)
    {{
        handler?.Invoke(res);
    }}
    else
    {{
        NKWebClientManager.Instance.OnCommonError(res.ProtocolId, res.result);
    }}

    return res;
}}
"""

packet = """public async UniTask<Res{name}> Request{name}Async({args}, Action<Res{name}> handler)
{{
    var res = await NetworkManager.Instance.Client.SendAsync<Res{name}>(
        new Req{name}
        {{
            usn = NKUserData.AccountData.USN,
        }});

    if (res.result == ResultCode.Success)
    {{
        handler?.Invoke(res);
    }}
    else
    {{
        NKWebClientManager.Instance.OnCommonError(res.ProtocolId, res.result);
    }}

    return res;
}}
"""

# ==================================================
#   Main
#       simple_packet
#       packet
# ==================================================
query = packet
name = "TouchEmergencyQuestInteractionObject"
args = "string positionId"

f = open(output_file_name, "w")
f.write(query.format(name = name, args = args))
f.close()