def samename(arr):
    d = {}
    a = set()
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] > 1:
            a.add(i)
    if len(a) > 0:
        return a
    return -1

arr = ["Tom", "Jerry", "Mike", "Curry", "Happy", "Tom", "Curry"]
if samename(arr) == -1:
    print("동명이인 없음")
else:
    print(samename(arr))
