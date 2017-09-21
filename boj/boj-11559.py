def solve(_map):
    from collections import deque
    q = deque([])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    all_combo = 0
    combo = 0
    start = False
    while start is False or combo != 0:
        start = True
        combo = 0
        visited = [[0]*6 for _ in range(12)]
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    continue
                ppuyo_with_same_color = []
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    ppuyo_with_same_color.append((y, x))
                    for direction in directions:
                        dy = y + direction[0]
                        dx = x + direction[1]
                        if dy < 0 or dx < 0 or dy >= 12 or dx >= 6 or visited[dy][dx] == 1:
                            continue
                        if _map[y][x] == _map[dy][dx] and _map[y][x] in 'RGBPY':
                            visited[dy][dx] = 1
                            q.append((dy, dx))
                if len(ppuyo_with_same_color) >= 4:
                    for y, x in ppuyo_with_same_color:
                        _map[y][x] = '.'
                    combo+=1
        for j in range(6):
            for i in range(1, 12):
                if _map[i][j] == '.':
                    for k in range(i, 0, -1):
                        temp = _map[k][j]
                        _map[k][j] = _map[k-1][j]
                        _map[k-1][j] = temp
        all_combo += combo > 0
    return all_combo

def run():
    import sys
    read = sys.stdin.readline
    _map = ['']*12
    for i in range(12):
        _map[i] = list(read().replace('\n', ''))
    print(solve(_map))

run()
