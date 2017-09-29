def find_zero(points):
    for i in range(3):
        for j in range(3):
            if points[i][j] == 0:
                return (i, j)

def get_differences(solution, points):
    ret = 0
    for i in range(3):
        for j in range(3):
           if solution[i][j] != 0 and solution[i][j] != points[i][j]:
               ret += 1
    return ret 

def solve(start):
    from collections import deque
    INF = 1e100
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([])
    solution = "123456780"
    visited = dict()
    # q.append((get_differences(solution, points), points, find_zero(points), 0))
    zero = start.index("0")
    q.append((start, 0, (zero//3 , zero%3)))
    
    ret = INF
    while q:
        # differences, points, (y, x), move = heapq.heappop(q)
        # differences, points, (y, x), move = q.popleft()
        cur, moves, (y, x) = q.popleft()
        i = 3 * y + x
        # differences, points, (y, x), move = q.pop(0)
        if cur in visited:
            continue
        # print(differences, points, (y, x), move)
        visited[cur] = 1
        if cur == solution:
            ret = min(ret, moves)
        for d in directions:
            dy = y + d[0]
            dx = x + d[1]
            di = 3 * dy + dx
            if dy < 0 or dx < 0 or dx > 2 or dy > 2:
                continue
            if i > di:
                _next = cur[:di] + cur[i:i+1] + cur[di+1:i] + cur[di:di+1] + cur[i+1:]
            else:
                _next = cur[:i] + cur[di:di+1] + cur[i+1:di] + cur[i:i+1] + cur[di+1:]
            q.append((_next, moves+1, (dy, dx)))
    if ret == INF:
        return -1
    return ret

def run():
    import sys
    read = sys.stdin.readline
    start = ""
    for _ in range(3):
        line = read().split()
        for e in line:
            start+=e
    print(solve(start))

run()
