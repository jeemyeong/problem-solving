def solve(alpha):
    ret = "Distances:"
    for i in range(len(alpha[0])):
        d = ord(alpha[1][i])-ord(alpha[0][i])
        if d < 0:
            d+=26
        ret += " "+str(d)
    return ret
    

def run():
    import sys
    read = sys.stdin.readline

    n = int(read().replace("\n", ""))
    for _ in range(n):
        print(solve(read().replace("\n", "").split()))

run()
