def solve(N, M, _map):
    from collections import deque
    R = None
    B = None
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 'R':
                R = (i, j)
                _map[i][j] = '.'
            elif _map[i][j] == 'B':
                B = (i, j)
                _map[i][j] = '.'
    q = deque([])
    moves = 0
    q.append((moves, R, B))
    visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    while q:
        moves, R, B = q.popleft()
        if visited[R[0]][R[1]][B[0]][B[1]] == 1 or moves >= 10:
            continue
        visited[R[0]][R[1]][B[0]][B[1]] = 1
        # Moves to up
        if R[0] >= B[0]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dB[0], 1, -1):
                if dR[0] == (dB[0]-1) and dR[1] == dB[1]:
                    break
                elif _map[dB[0]-1][dB[1]] == '.':
                    dB[0] -= 1
                elif _map[dB[0]-1][dB[1]] == '#':
                    break
                elif _map[dB[0]-1][dB[1]] == 'O':
                    blue_into_the_hole = True
                    break
            for i in range(dR[0], 1, -1):
                if (dR[0]-1) == dB[0] and dR[1] == dB[1]:
                    break
                elif _map[dR[0]-1][dR[1]] == '.':
                    dR[0] -= 1
                elif _map[dR[0]-1][dR[1]] == '#':
                    break
                elif _map[dR[0]-1][dR[1]] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))
        elif B[0] > R[0]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dR[0], 1, -1):
                if (dR[0]-1) == dB[0] and dR[1] == dB[1]:
                    break
                elif _map[dR[0]-1][dR[1]] == '.':
                    dR[0] -= 1
                elif _map[dR[0]-1][dR[1]] == '#':
                    break
                elif _map[dR[0]-1][dR[1]] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            for i in range(dB[0], 1, -1):
                if dR[0] == (dB[0]-1) and dR[1] == dB[1]:
                    break
                elif _map[dB[0]-1][dB[1]] == '.':
                    dB[0] -= 1
                elif _map[dB[0]-1][dB[1]] == '#':
                    break
                elif _map[dB[0]-1][dB[1]] == 'O':
                    blue_into_the_hole = True
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))

        # Moves to down
        if R[0] <= B[0]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dB[0], N-1, 1):
                if dR[0] == (dB[0]+1) and dR[1] == dB[1]:
                    break
                elif _map[dB[0]+1][dB[1]] == '.':
                    dB[0] += 1
                elif _map[dB[0]+1][dB[1]] == '#':
                    break
                elif _map[dB[0]+1][dB[1]] == 'O':
                    blue_into_the_hole = True
                    break
            for i in range(dR[0], N-1, 1):
                if (dR[0]+1) == dB[0] and dR[1] == dB[1]:
                    break
                elif _map[dR[0]+1][dR[1]] == '.':
                    dR[0] += 1
                elif _map[dR[0]+1][dR[1]] == '#':
                    break
                elif _map[dR[0]+1][dR[1]] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))
        elif B[0] < R[0]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dR[0], N-1, 1):
                if (dR[0]+1) == dB[0] and dR[1] == dB[1]:
                    break
                elif _map[dR[0]+1][dR[1]] == '.':
                    dR[0] += 1
                elif _map[dR[0]+1][dR[1]] == '#':
                    break
                elif _map[dR[0]+1][dR[1]] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            for i in range(dB[0], N-1, 1):
                if dR[0] == (dB[0]+1) and dR[1] == dB[1]:
                    break
                elif _map[dB[0]+1][dB[1]] == '.':
                    dB[0] += 1
                elif _map[dB[0]+1][dB[1]] == '#':
                    break
                elif _map[dB[0]+1][dB[1]] == 'O':
                    blue_into_the_hole = True
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))

        # Moves to left
        if R[1] >= B[1]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dB[1], 1, -1):
                if dR[0] == dB[0] and dR[1] == (dB[1]-1):
                    break
                elif _map[dB[0]][dB[1]-1] == '.':
                    dB[1] -= 1
                elif _map[dB[0]][dB[1]-1] == '#':
                    break
                elif _map[dB[0]][dB[1]-1] == 'O':
                    blue_into_the_hole = True
                    break
            for i in range(dR[1], 1, -1):
                if dR[0] == dB[0] and (dR[1]-1) == dB[1]:
                    break
                elif _map[dR[0]][dR[1]-1] == '.':
                    dR[1] -= 1
                elif _map[dR[0]][dR[1]-1] == '#':
                    break
                elif _map[dR[0]][dR[1]-1] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))
        elif B[1] > R[1]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dR[1], 1, -1):
                if dR[0] == dB[0] and (dR[1]-1) == dB[1]:
                    break
                elif _map[dR[0]][dR[1]-1] == '.':
                    dR[1] -= 1
                elif _map[dR[0]][dR[1]-1] == '#':
                    break
                elif _map[dR[0]][dR[1]-1] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            for i in range(dB[1], 1, -1):
                if dR[0] == dB[0] and dR[1] == (dB[1]-1):
                    break
                elif _map[dB[0]][dB[1]-1] == '.':
                    dB[1] -= 1
                elif _map[dB[0]][dB[1]-1] == '#':
                    break
                elif _map[dB[0]][dB[1]-1] == 'O':
                    blue_into_the_hole = True
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))

        # Moves to right
        if R[1] <= B[1]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dB[1], M-1, 1):
                if dR[0] == dB[0] and dR[1] == (dB[1]+1):
                    break
                elif _map[dB[0]][dB[1]+1] == '.':
                    dB[1] += 1
                elif _map[dB[0]][dB[1]+1] == '#':
                    break
                elif _map[dB[0]][dB[1]+1] == 'O':
                    blue_into_the_hole = True
                    break
            for i in range(dR[1], M-1, 1):
                if dR[0] == dB[0] and (dR[1]+1) == dB[1]:
                    break
                elif _map[dR[0]][dR[1]+1] == '.':
                    dR[1] += 1
                elif _map[dR[0]][dR[1]+1] == '#':
                    break
                elif _map[dR[0]][dR[1]+1] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))
        elif B[1] < R[1]:
            dR = [R[0], R[1]]
            dB = [B[0], B[1]]
            red_into_the_hole = False
            blue_into_the_hole = False
            for i in range(dR[1], M-1, 1):
                if dR[0] == dB[0] and (dR[1]+1) == dB[1]:
                    break
                elif _map[dR[0]][dR[1]+1] == '.':
                    dR[1] += 1
                elif _map[dR[0]][dR[1]+1] == '#':
                    break
                elif _map[dR[0]][dR[1]+1] == 'O':
                    red_into_the_hole = True
                    dR = (-1, -1)
                    break
            for i in range(dB[1], M-1, 1):
                if dR[0] == dB[0] and dR[1] == (dB[1]+1):
                    break
                elif _map[dB[0]][dB[1]+1] == '.':
                    dB[1] += 1
                elif _map[dB[0]][dB[1]+1] == '#':
                    break
                elif _map[dB[0]][dB[1]+1] == 'O':
                    blue_into_the_hole = True
                    break
            if blue_into_the_hole is False and red_into_the_hole is True:
                return moves+1
            if red_into_the_hole is False and blue_into_the_hole is False:
                q.append((moves+1, (dR[0], dR[1]), (dB[0], dB[1])))
    return -1

def run():
    import sys
    read = sys.stdin.readline
    N, M = map(int, read().split())
    _map = []
    for _ in range(N):
        _map.append(list(read().replace("\n", "")))
    print(solve(N, M, _map))

run()
