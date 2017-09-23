# Not solved

def solve(K, files):
    print(files)
    ret = 0
    for _ in range(K-1):
        # print(files)
        files.sort()
        min1 = files.pop(files.index(min(files)))
        min2 = files.pop(files.index(min(files)))
        ret += min1 + min2
        # print(min1, min2, ret)
        print(files, end=", ")
        files.append(min1+min2)
        print(files, ret)
    print(files)
    return ret

def run():
    import sys
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        K = int(read())
        files = list(map(int, read().split()))
        print(solve(K, files))

run()
