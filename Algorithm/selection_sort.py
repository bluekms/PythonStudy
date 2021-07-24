from typing import List


def GetMinIndex(arr: List[str]) -> int:
    minIndex = 0
    for i in range(len(arr)):
        if arr[i] < arr[minIndex]:
            minIndex = i
    return minIndex


def SelectionSort(arr: List[str]) -> List[str]:
    result = []
    while input:
        minIndex = GetMinIndex(arr)
        result.append(arr.pop(minIndex))
    return result


input = ["개구리", "거위", "고릴라", "기린", "닭", "말", "북극곰", "얼룩말", "코끼리"]
print(SelectionSort(input))
