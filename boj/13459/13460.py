def move(grid, cur, d, R, B):
    while True:
        if grid[cur[0]+d[0]][cur[1]+d[1]] == '#' or (cur[0]+d[0], cur[1]+d[1]) in (R, B):
            return cur
        if grid[cur[0]+d[0]][cur[1]+d[1]] == 'O':
            return (-1, -1)
        cur = (cur[0]+d[0], cur[1]+d[1])

def solve(N, M, grid):
    from collections import deque
    R = None
    B = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'R':
                R = (i, j)
            elif grid[i][j] == 'B':
                B = (i, j)

    q = deque([])
    q.append((R, B))
    visited = set()
    for moves in range(10):
        for _ in range(len(q)):
            R, B = q.popleft()
            if (R, B) in visited:
                continue
            visited.add((R, B))
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dR = move(grid, R, d, R, B)
                dB = move(grid, B, d, dR, B)
                dR = move(grid, dR, d, dR, dB)
                if dB == (-1, -1):
                    continue
                if dR == (-1, -1):
                    return moves+1
                q.append((dR, dB))
    return -1

def run():
    import sys
    read = sys.stdin.readline
    N, M = map(int, read().split())
    grid = []
    for _ in range(N):
        grid.append(list(read().replace("\n", "")))
    print(solve(N, M, grid))

run()
