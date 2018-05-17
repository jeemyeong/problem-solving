import sys

def LS(): return sys.stdin.readline().split()

def solve(n, m, lst):
    available = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        for (c, p) in lst:
            if i >= p:
                available[i] = max(available[i], available[i-p]+c)
    return available[m]

def main():
    while True:
        n, m = LS()
        n = int(n)
        m = int(100*float(m))
        if (n, m) == (0, 0):
            return
        lst = []
        for _ in range(n):
            c, p = LS()
            c = int(c)
            p = int(100*float(p))
            lst.append((c, p))
        
        print(solve(n, m, lst))

main()
