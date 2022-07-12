# a = {17, 92, 18, 58, 7, 33, 42}

# def Max(a):
#     max = a[0]
#     for x in range(len(a)):
#         if max < a[x]:
#             max = a[x]
#     return max

# def Max_index(a):
#     max = a[0]
#     max_index = 0
#     for x in range(len(a)):
#         if max < a[x]:
#             max = a[x]
#             max_index = x
#     return max_index
# print('max is %d'%(Max(a)))
# print('maxindex is %d'%(Max_index(a)))

# print('max is %d'%(max(a)))
# print('maxindex is %d'%(a.index(max(a))))

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

def same_name(a):
    s = set()
    n = len(a)
    for x in range(n - 1):
        for y in range(x + 1, n):
            if a[x] == a[y]:
                s.add(a[x])
    return s
print(same_name(name)[0])

