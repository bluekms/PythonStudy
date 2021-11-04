# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/NKWebClient.cs"

sender = """public async UniTask<Res{_name}> Request{_name}Async(Action<Res{_name}> handler)
{{
    var res = await NetworkManager.Instance.Client.SendAsync<Res{_name}>(
        new Req{_name}
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
#   Set Arguments
#       sender
# ==================================================
query = sender
_name = "ObtainMessageReward"

f = open(output_file_name, "w")
f.write(query.format(_name=_name))
f.close()
