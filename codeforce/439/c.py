# Not solved

import sys
import heapq, collections

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

def solve(a, b, c):
    ret = 0
    c0, c1, c2 = sorted([a, b, c])
    q = collections.deque([])
    q.append(([c0, c1, c2], 1, 0, 1))
    q.append(([c0, c1, c2], 1, 0, 2))
    while q:
        not_visited, cnt, cur, following = q.popleft()
        if not_visited[cur] == 0:
            continue
        cnt *= not_visited[cur]
        not_visited[cur] -= 1
        c0, c1, c2 = not_visited
        ret += cnt
        q.append(([c0, c1, c2], cnt, following, 3 - cur - following))




    return ret

def run():
    a, b, c = LI()
    print(solve(a, b, c))

run()
