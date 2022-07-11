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

s = set()
s.add(3)
s.add(2)
s.add(1)
s.add(3)
print(s)
