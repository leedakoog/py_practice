def maze_sol(maze_info, start, end):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        print(qu)
        p = qu.pop(0)
        print(p)
        v = p[-1]
        if v == end:
            return p
        for x in maze_info[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)
    return "?"

maze_info = {
    'a': ['e'],
    'e': ['a', 'i'],
    'i': ['e', 'm'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'j': ['n', 'k', 'f'],
    'k': ['j', 'o'],
    'o': ['k'],
    'f': ['j', 'g', 'b'],
    'b': ['f', 'c'],
    'c': ['b', 'd'],
    'd': ['c'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'l': ['h', 'p'],
    'p': ['l']
}
print(maze_sol(maze_info, 'a', 'p'))
