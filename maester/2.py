def solution(maps):
    from collections import deque
    max_y = len(maps) - 1
    max_x = len(maps[0]) - 1
    DIRECTIONS = [
        {
            "dy": 1,
            "dx": 0
        },
        {
            "dy": -1,
            "dx": 0
        },
        {
            "dy": 0,
            "dx": 1
        },
        {
            "dy": 0,
            "dx": -1
        },
    ]
    start = {
        "y": 0,
        "x": 0,
        "count": 1
    }
    q = deque([start])
    visited = [[False] * (max_x+1) for _ in range(max_y+1)]
    visited[start["y"]][start["x"]] = 0
    while q:
        cur = q.popleft()
        if visited[cur["y"]][cur["x"]] is True:
            continue
        visited[cur["y"]][cur["x"]] = True
        if cur["y"] == max_y and cur["x"] == max_x:
            return cur["count"]
        for DIRECTION in DIRECTIONS:
            next_cur = {
                "y": cur["y"] + DIRECTION["dy"],
                "x": cur["x"] + DIRECTION["dx"],
                "count": cur["count"]+1
            }
            if next_cur["y"] < 0 or next_cur["y"] > max_y or next_cur["x"] < 0 or next_cur["x"] > max_x:
                continue
            if maps[next_cur["y"]][next_cur["x"]] == 0:
                continue
            q.append(next_cur)
    
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))