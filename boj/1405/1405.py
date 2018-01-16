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

def check(y, x, visited):
    if (y, x) in visited and visited[(y, x)] is True:
        return True
    return False

def dfs(N, y, x, dirs, visited):
    if N < 0:
        return 1
    if check(y, x, visited):
        return 0
    visited[(y, x)] = True
    ret = 0
    for dy, dx, PROB in dirs:
        ret += PROB * dfs(N-1, y+dy, x+dx, dirs, visited)
    visited[(y, x)] = False
    return ret

def solve(N, dirs, visited):
    return dfs(N, 0, 0, dirs, visited) / (100 ** (N+1))

def main():
    N, E_PROB, W_PROB, S_PROB, N_PROB = LI()
    dirs = (0, -1, E_PROB), (0, +1, W_PROB), (+1, 0, S_PROB), (-1, 0, N_PROB)
    visited = {}
    print(solve(N, dirs, visited))

main()
