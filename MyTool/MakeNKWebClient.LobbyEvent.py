# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/NKWebClient.LobbyEvent.cs"

simple_packet = """public async UniTask<Res{name}> Request{name}Async(Action<Res{name}> handler)
{{
    var res = await NetworkManager.Instance.Client.SendAsync<Res{name}>(
        new Req{name}
        {{
            Usn = NKUserData.AccountData.USN,
        }});

    if (res.Result == ResultCode.Success)
    {{
        handler?.Invoke(res);
    }}
    else
    {{
        NKWebClientManager.Instance.OnCommonError(res.ProtocolId, res.Result);
    }}

    return res;
}}
"""

packet = """public async UniTask<Res{name}> Request{name}Async({args}, Action<Res{name}> handler)
{{
    var res = await NetworkManager.Instance.Client.SendAsync<Res{name}>(
        new Req{name}
        {{
            Usn = NKUserData.AccountData.USN,
        }});

    if (res.Result == ResultCode.Success)
    {{
        handler?.Invoke(res);
    }}
    else
    {{
        NKWebClientManager.Instance.OnCommonError(res.ProtocolId, res.Result);
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
name = "SetTutorial"
args = ""

f = open(output_file_name, "w")
f.write(query.format(name = name, args = args))
f.close()