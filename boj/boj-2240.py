# Not solved
def solve(T, W, order):
    import heapq
    q = []
    heapq.heappush(q, (W, 1 if 1 == order[0] else 0, 0, 1))
    heapq.heappush(q, (W, 1 if 2 == order[0] else 0, 0, 2))
    dp = [[[0]*2 for _ in range(W+1)] for _ in range(T)]
    while q:
        left_w, count, index, position = heapq.heappop(q)
        if count < dp[index][left_w][position-1]:
            continue
        dp[index][left_w][position-1] = count
        if index == T-1:
            continue
        if position == 1:
            heapq.heappush(q, (left_w, count + (1 if order[index+1] == 1 else 0), index+1, 1))
            if left_w > 0:
                heapq.heappush(q, (left_w-1, count + (1 if order[index+1] == 2 else 0), index+1, 2))
        if position == 2:
            heapq.heappush(q, (left_w, count + (1 if order[index+1] == 2 else 0), index+1, 2))
            if left_w > 0:
                heapq.heappush(q, (left_w-1, count + (1 if order[index+1] == 1 else 0), index+1, 1))
    # for i in dp:
    #     print(i)
    # print()
    return max(max(dp[T-1], key=lambda x: max(x)))

def run():
    import sys
    read = sys.stdin.readline
    T, W = map(int, read().split())
    order = []
    for _ in range(T):
        order.append(int(read()))
    print(solve(T, W, order))

run()
