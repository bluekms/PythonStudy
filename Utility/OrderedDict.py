from collections import OrderedDict

oneDict = {"one": 1, "two": 2, "three": 3}
d = OrderedDict(oneDict)
print(d)

# 해당 key를 가장 뒤로 보낸다
d.move_to_end("one")
print(d)

# 해당 key를 가장 앞으로 보낸다
d.move_to_end("one", False)
print(d)

# 가장 뒤 아이템을 꺼낸다
# d.popitem()
out = d.popitem(True)
print(out)
print(d)

# 가장 앞 아이템을 꺼낸다
out = d.popitem(False)
print(out)
print(d)
