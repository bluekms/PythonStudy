from typing import List

def MergeSort(arr: List[str]) -> List[str]:
    length = len(arr)
    if (length <= 1):
        return arr

    centerIndex = length // 2
    arr1 = MergeSort(arr[:centerIndex])
    arr2 = MergeSort(arr[centerIndex:])
    result = []

    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    while arr1:
        result.append(arr1.pop(0))

    while arr2:
        result.append(arr2.pop(0))
        
    return result

input = ['기린', '얼룩말', '코끼리', '개구리', '닭', '말', '북극곰', '거위', '고릴라']
print(MergeSort(input))