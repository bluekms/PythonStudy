from typing import List

def QuickSort(arr: List[str]) -> List[str]:
    length = len(arr)
    if length <= 1:
        return arr

    pivot = arr[-1]
    arr1 = []
    arr2 = []
    for i in range(length - 1):
        if arr[i] < pivot:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])

    return QuickSort(arr1) + [pivot] + QuickSort(arr2)

input = ['기린', '얼룩말', '코끼리', '개구리', '닭', '말', '북극곰', '거위', '고릴라']
print(QuickSort(input))