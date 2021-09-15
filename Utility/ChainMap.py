from collections import ChainMap

oneDict = {"one": 1, "two": 2, "three": 3}
towDict = {"four": 4}

# ChainMap({'one': 1, 'two': 2, 'three': 3}, {'four': 4})
chain = ChainMap(oneDict, towDict)
print(chain)

"one" in chain  # True
"five" in chain  # False
len(chain)  # 4

# ChainMap은 아이템의 Type을 유지하기 때문에 적절치 않다
chain.values()
chain.keys()
chain.items()
chain.maps[0]  # chain[0], chain["oneDict"]는 error
