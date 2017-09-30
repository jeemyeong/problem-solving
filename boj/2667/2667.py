def solve(N, _map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0]*N for _ in range(N)]
    ret = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            if _map[i][j] == '0':
                visited[i][j] = 1
                continue
            q = []
            q.append((i, j))
            count = 0
            while q:
                y, x = q.pop()
                if visited[y][x] == 1:
                    continue
                visited[y][x] = 1
                count += 1
                for d in directions:
                    dy = y + d[0]
                    dx = x + d[1]
                    if dy < 0 or dx < 0 or dy >= N or dx >= N or _map[y][x] != _map[dy][dx]:
                        continue
                    q.append((dy, dx))
            ret.append(count)
    ret = [len(ret)] + sorted(ret)
    return '\n'.join(map(str, ret))

def run():
    import sys
    read = sys.stdin.readline
    N = int(read().replace("\n", ""))
    _map = []
    for _ in range(N):
        _map.append(read().replace("\n", ""))
    print(solve(N, _map))

run()
