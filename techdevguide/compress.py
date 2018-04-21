def solve(text):
    a = 0
    b = 0
    length = len(text)
    ret = ""
    number = 1
    while b < length:
        if a == b:
            b += 1
            continue
        if cur[b] == cur[a]:
            number += 1
            continue
        if cur[b] != cur[a]:
            

    
    return string

print(solve("abcabcabcababababc"))
print(solve("aaabaaab"))