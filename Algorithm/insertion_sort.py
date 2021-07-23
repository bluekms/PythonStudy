from typing import List

def FindIndex(arr:List[str], value: str) -> int:
    for i in range(len(arr)):
        if value < arr[i]:
            return i
    return len(arr)

def InsertionSort(arr: List[str]) -> List[str]:
    result = []
    while arr:
        value = arr.pop(0)
        index = FindIndex(result, value)
        result.insert(index, value)
    return result

input = ['기린', '얼룩말', '코끼리', '개구리', '닭', '말', '북극곰', '거위', '고릴라']
print(InsertionSort(input))