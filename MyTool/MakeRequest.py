# ==================================================
#   Detail
# ==================================================
output_file_name = "./MyTool/build/NKWebClient.LobbyEvent.cs"

Foo = """public async UniTask<Res{name}> Request{name}Async(, Action<Res{name}> handler)
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
#   Set Arguments
#       Foo
# ==================================================
query = Foo
name = "SubQuestMessengerTriggersRuleCheckerRule"

f = open(output_file_name, "w")
f.write(query.format(name=name))
f.close()
