def max_profit1(stock):   # -------> 시간복잡도 n제곱
    n = len(stock)
    max = stock[1] - stock[0]
    for x in range(n):
        for y in range(x + 1, n):
            st_max = stock[y] - stock[x]
            if st_max > max:
                max = st_max
    return max

def max_profit2(stock):   # -------> 시간복잡도 n
    n = len(stock)
    max = 0
    min = stock[0]
    for x in range(1, n):
        st = stock[x] - min
        if st > max:
            max = st
        if stock[x] < min:
            min = stock[x]
    return max

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit1(stock))
print(max_profit2(stock))