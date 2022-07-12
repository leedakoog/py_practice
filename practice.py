name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

def same_name(a):
    s = set()
    n = len(a)
    for x in range(n - 1):
        for y in range(x + 1, n):
            if a[x] == a[y]:
                s.add(a[x])
    return s
print(same_name(name))

