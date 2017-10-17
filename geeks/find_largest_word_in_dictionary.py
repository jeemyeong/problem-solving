import sys
# import heapq, collections

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def solve(N, x, s):
    ret = max(x, key=lambda x: len(x) if check(x, s) else 0)
    return ret

def check(dict_s, str_s):
    _from = 0
    for i in dict_s:
        if i in str_s[_from:]:
            _from += str_s[_from:].index(i) + 1
            continue
        else:
            return False
    return True

def main():
    T = I()
    for _ in range(T):
        N = I()
        x = LS()
        s = S()
        print(solve(N, x, s))

main()
