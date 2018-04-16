import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def S(): return input()

def solve(n, a, b, lst):
    ret = 0
    for i in lst:
        if i % 2 == 0:
            cnt = min(a, i//2)
            ret += cnt
            a -= cnt
            cnt = min(b, i//2)
            ret += cnt
            b -= cnt
        elif a > b:
            cnt = min(a, i//2 + 1)
            ret += cnt
            a -= cnt
            cnt = min(b, i//2)
            ret += cnt
            b -= cnt
        elif b >= a:
            cnt = min(a, i//2)
            ret += cnt
            a -= cnt
            cnt = min(b, i//2 + 1)
            ret += cnt
            b -= cnt
            
    
    return ret

def main():
    n, a, b = LI()
    lst = S()
    print(solve(n, a, b, sorted(map(len, filter(lambda x: len(x) > 0 , lst.split("*"))), reverse=True)))

main()