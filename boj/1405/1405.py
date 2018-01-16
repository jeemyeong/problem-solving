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

def solve(N, dx, dy, PROB):
    stack = []; visited = {};
    res = 0; y = 0; x = 0;
    cur = {
        "y": y,
        "x": x,
        "P": 1,
        "k": 0
    }
    visited[(0, 0)] = True
    stack.append(cur)
    while stack:
        cur_point = stack[-1]
        if len(stack) == N+1:
            res += cur_point["P"]
            stack.pop()
            visited[(cur_point["y"], cur_point["x"])] = False
            continue
        if cur_point["k"] == 4:
            stack.pop()
            visited[(cur_point["y"], cur_point["x"])] = False
            continue
        next_point = {
            "y": cur_point["y"] + dy[cur_point["k"]],
            "x": cur_point["x"] + dx[cur_point["k"]],
            "P": cur_point["P"] * PROB[cur_point["k"]] / 100,
            "k": 0
        }
        cur_point["k"] += 1
        if check(next_point["y"], next_point["x"], visited) is False:
            stack.append(next_point)
            visited[(next_point["y"], next_point["x"])] = True
    return res

def main():
    N, E_PROB, W_PROB, S_PROB, N_PROB = LI()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    PROB = [E_PROB, W_PROB, S_PROB, N_PROB]
    print(solve(N, dx, dy, PROB))

main()
