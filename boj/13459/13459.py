def solve(N, M, _map):
    from collections import deque
    q = deque([])
    q.append((_map, 0))
    visited = dict()
    while q:
        _map, moves = q.popleft()
        if str(_map) in visited or moves >= 10:
            continue
        visited[str(_map)] = 1
        new_map = [[e for e in row] for row in _map]
        red_into_the_hole = False
        blue_into_the_hole = False
        for i in range(0, N-1):
            for j in range(0, M-1):
                for k in range(i, 0, -1):
                    if new_map[k][j] != 'R' and new_map[k][j] != 'B':
                        break
                    if new_map[k-1][j] == '.':
                        temp = new_map[k][j]
                        new_map[k][j] = new_map[k-1][j]
                        new_map[k-1][j] = temp
                    elif new_map[k][j] == 'R' and new_map[k-1][j] == 'O':
                        new_map[k][j] = '.'
                        red_into_the_hole = True
                    elif new_map[k][j] == 'B' and new_map[k-1][j] == 'O':
                        new_map[k][j] = '.'
                        blue_into_the_hole = True
        if red_into_the_hole is True and blue_into_the_hole is False:
            return 1
        if red_into_the_hole is False and blue_into_the_hole is False:
            q.append((new_map, moves+1))
        
        new_map = [[e for e in row] for row in _map]
        red_into_the_hole = False
        blue_into_the_hole = False
        for i in range(N-1, 0, -1):
            for j in range(M-1, 0, -1):
                for k in range(i, N, 1):
                    if new_map[k][j] != 'R' and new_map[k][j] != 'B':
                        break
                    if new_map[k+1][j] == '.':
                        temp = new_map[k][j]
                        new_map[k][j] = new_map[k+1][j]
                        new_map[k+1][j] = temp
                    elif new_map[k][j] == 'R' and new_map[k+1][j] == 'O':
                        new_map[k][j] = '.'
                        red_into_the_hole = True
                    elif new_map[k][j] == 'B' and new_map[k+1][j] == 'O':
                        new_map[k][j] = '.'
                        blue_into_the_hole = True
        if red_into_the_hole is True and blue_into_the_hole is False:
            return 1
        if red_into_the_hole is False and blue_into_the_hole is False:
            q.append((new_map, moves+1))

        new_map = [[e for e in row] for row in _map]
        red_into_the_hole = False
        blue_into_the_hole = False
        for i in range(0, N-1):
            for j in range(0, M-1):
                for k in range(j, 0, -1):
                    if new_map[i][k] != 'R' and new_map[i][k] != 'B':
                        break
                    if new_map[i][k-1] == '.':
                        temp = new_map[i][k]
                        new_map[i][k] = new_map[i][k-1]
                        new_map[i][k-1] = temp
                    elif new_map[i][k] == 'R' and new_map[i][k-1] == 'O':
                        new_map[i][k] = '.'
                        red_into_the_hole = True
                    elif new_map[i][k] == 'B' and new_map[i][k-1] == 'O':
                        new_map[i][k] = '.'
                        blue_into_the_hole = True
        if red_into_the_hole is True and blue_into_the_hole is False:
            return 1
        if red_into_the_hole is False and blue_into_the_hole is False:
            q.append((new_map, moves+1))
        
        new_map = [[e for e in row] for row in _map]
        red_into_the_hole = False
        blue_into_the_hole = False
        for i in range(N-1, 0, -1):
            for j in range(M-1, 0, -1):
                for k in range(j, M, 1):
                    if new_map[i][k] != 'R' and new_map[i][k] != 'B':
                        break
                    if new_map[i][k+1] == '.':
                        temp = new_map[i][k]
                        new_map[i][k] = new_map[i][k+1]
                        new_map[i][k+1] = temp
                    elif new_map[i][k] == 'R' and new_map[i][k+1] == 'O':
                        new_map[i][k] = '.'
                        red_into_the_hole = True
                    elif new_map[i][k] == 'B' and new_map[i][k+1] == 'O':
                        new_map[i][k] = '.'
                        blue_into_the_hole = True
        if red_into_the_hole is True and blue_into_the_hole is False:
            return 1
        if red_into_the_hole is False and blue_into_the_hole is False:
            q.append((new_map, moves+1))


    return 0

def run():
    import sys
    read = sys.stdin.readline
    N, M = map(int, read().split())
    _map = []
    for _ in range(N):
        _map.append(list(read().replace("\n", "")))
    print(solve(N, M, _map))

run()
