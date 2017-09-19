def dfs(N, M, V, edges, dfs_visited):
    if dfs_visited[V] == 1:
        return []
    dfs_visited[V] = 1
    ret = [V]
    for dv in edges[V]:
        ret += dfs(N, M, dv, edges, dfs_visited)
    return ret

def bfs(N, M, V, edges):
    from collections import deque
    bfs_visited = [0] * (N+1)
    q = deque()
    q.append(V)
    ret = []
    while q:
        u = q.popleft()
        if bfs_visited[u] == 1:
            continue
        bfs_visited[u] = 1
        ret.append(u)
        for dv in edges[u]:
            q.append(dv)
    return ret

def run():
    import sys
    read = sys.stdin.readline
    N, M, V = map(int, read().split())
    edges = dict([[i, []] for i in range(N+1)])
    for _ in range(M):
        u1, u2 = map(int, read().split())
        edges[u1].append(u2)
        edges[u2].append(u1)
    for each_V in edges:
        edges[each_V].sort()
    dfs_visited = [0] * (N+1)
    print(" ".join(map(str, dfs(N, M, V, edges, dfs_visited))))
    print(" ".join(map(str, bfs(N, M, V, edges))))

run()
