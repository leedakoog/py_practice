def binary_search(arr, value):
    n = len(arr)
    f = 0
    e = n - 1
    while True:
        mid = (f + e) // 2
        if arr[mid] == value:
            break
        elif arr[mid] < value:
            f = mid + 1
        else:
            e = mid - 1
    return mid

arr = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(arr, 9))