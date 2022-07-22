from unittest import result


def find_min(arr):
    n = len(arr)
    min_idx = 0
    for i in range(1, n):
        if arr[min_idx] > arr[i]:
            min_idx = i
    return min_idx

def sort(arr):
    n = len(arr)
    sort_list = []
    while arr:
        min_idx = find_min(arr)
        val = arr.pop(min_idx)
        sort_list.append(val)
    print("arr ->", arr)
    return sort_list


arr = [2, 4, 5, 3 ,1]
print(sort(arr))