def merge_sort(arr1, arr2):
    ar1 = sel_sort(arr1)
    ar2 = sel_sort(arr2)
    list = []
    n = 0
    while ar1 and ar2:
        if ar1[0] > ar2[0]:
            list.append(ar2.pop(0))
        else: list.append(ar1.pop(0))
    while ar1:
        list.append(ar1.pop(0))
    while ar2:
        list.append(ar2.pop(0))
    return list

def sel_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [5, 3, 2, 1, 4, 6]
n = len(arr) // 2
arr1 = arr[:n]
arr2 = arr[n:]
print(merge_sort(arr1, arr2))



