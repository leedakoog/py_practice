def palindrome(arr):
    ar = []

    for i in arr:
        ar.append(i)


    while ar:
        if len(ar) == 1:
            return 1
        if ar.pop(0) != ar.pop():
            return -1
    return 1
        
if palindrome("wertrew") == 1:
    print("회문이 맞습니다.")
else:
    print("회문이 아닙니다.")

