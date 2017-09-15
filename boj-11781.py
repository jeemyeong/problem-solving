INF = 1e100
def solve(distance, late, N, S, E):
    import heapq
    times = [INF] * (N+1)
    times[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        from_time, from_idx = heapq.heappop(q)
        for to_idx, from_to_distance in distance[from_idx]:
            rush_hour = late[from_idx][to_idx] and from_time < E and from_time + from_to_distance > S
            to_time = from_time

            if not rush_hour:
                to_time += from_to_distance

            if rush_hour and from_time < S and from_to_distance - (S - from_time) < (E-S) / 2:
                to_time += (S-from_time) + (from_to_distance - (S - from_time)) * 2
            elif rush_hour and from_time < S and from_to_distance - (S - from_time) >= (E-S) / 2:
                to_time += (S-from_time) + (E - S) + (from_to_distance - (S - from_time) - (E-S) / 2)
            elif rush_hour and from_time >= S and from_to_distance < (E-from_time) / 2:
                to_time += from_to_distance * 2
            elif rush_hour and from_time >= S and from_to_distance >= (E-from_time) / 2:
                to_time += (E-from_time) + (from_to_distance - (E - from_time) / 2)

            if times[to_idx] > to_time:
                times[to_idx] = to_time
                heapq.heappush(q, (times[to_idx], to_idx))
    ret = max(times[1:])
    if int(ret) == ret:
        return int(ret)
    return ret
    

def run():
    import sys
    read = sys.stdin.readline
    N, M, S, E = map(int, read().split())
    distance = dict([[i, []] for i in range(N+1)])
    late = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        A, B, L, t1, t2 = map(int, read().split())
        distance[A].append((B,L))
        distance[B].append((A,L))
        late[A][B] = t1
        late[B][A] = t2
    print(solve(distance, late, N, S, E))

run()