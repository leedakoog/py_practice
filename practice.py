def hanoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    hanoi(n - 1, a, c, b)
    print(a, "->", c)
    hanoi(n - 1, b, a, c)
print("n = 1")
hanoi(1, 1, 2, 3)
print("n = 2")
hanoi(2, 1, 2, 3)
print("n = 3")
hanoi(3, 1, 2, 3)
print("n = 4")
hanoi(4, 1, 2, 3)
