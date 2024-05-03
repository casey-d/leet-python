# pass in an array
# return the index of the two items in the array that add up to the target
from typing import List


def twosum_ineff(arr, target):
    result = []
    for idx, item in enumerate(arr):
        for j in range(idx + 1, len(arr)):
            temp = item + arr[j]
            if (temp == target):
                result = [idx, j]
                break
        if (len(result) > 0):
            break
    return result

def twosum_typed(arr:List[int],target:int) -> List[int]:
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j]==target):
                return [i,j]
    return []


def twosum_eff(arr, target):
    result = []
    map = {}
    for idx, item in enumerate(arr):
        need = target - item
        if need in map:
            result = [map.get(need), idx]
        else:
            map[item] = idx
    return result

def twosum_eff_typed(arr:List[int],target:int)->List[int]:
    map={}
    for idx,item in enumerate(arr):
        need = target-item
        if need in map:
            return [map.get(need,idx)]
        else:
            map[item]=idx
    return []

nums = [2, 7, 11, 15];
target = 9;
result = twosum_ineff(nums, target)
print(result)
result2 = twosum_eff(nums, target)
result3 = twosum_typed(nums, target)
print(result3)
result4 = twosum_eff_typed(nums, target)

print(result4)
