def fr_of_fr(friend_info, friend):
    qu = []
    done = []

    qu.append(friend)
    done.append(friend)

    while qu:
        p = qu.pop(0)
        print(p)
        for x in friend_info[p]:
            if x not in done:
                qu.append(x)
                done.append(x)

friend_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}
fr_of_fr(friend_info, 'Summer')
print()
fr_of_fr(friend_info, 'Jerry')