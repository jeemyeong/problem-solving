import sys
inf = 10**20

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def TPS(cur, visited, cache, dist, N):
    if visited == (1<<N)-1:
        return dist[cur][0]
    if cache[cur][visited] != 0:
        return cache[cur][visited]
    ret = inf
    for next in range(N):
        if visited & 1 << next:
            continue
        if dist[cur][next] == 0:
            continue
        ret = min(ret, TPS(next, visited | (1 << next), cache, dist, N) + dist[cur][next])
    cache[cur][visited] = ret
    return ret

def solve(N, dist):
    cache = [[0 for _ in range(1 << N)] for _ in range(N)]
    return TPS(0, 1, cache, dist, N)

def main():
    N = I()
    dist = [LI() for _ in range(N)]
    print(solve(N, dist))

main()
