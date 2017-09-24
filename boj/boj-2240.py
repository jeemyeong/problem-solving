def get_item_without_null_exception(i, k, p, dp):
    if i < 0 or k < 0 or p < 0:
        return 0
    else:
        return dp[i][k][p]

def solve(T, W, order):
    dp = [[[0]*2 for _ in range(W+1)] for _ in range(T)]

    for i in range(0, T):
        for k in range(W+1):
            if order[i] == 1:
                dp[i][k][0] = max(get_item_without_null_exception(i-1, k, 0, dp), get_item_without_null_exception(i-1, k-1, 1, dp)) + 1
                dp[i][k][1] = max(get_item_without_null_exception(i-1, k, 1, dp), get_item_without_null_exception(i-1, k-1, 0, dp))
            else:
                dp[i][k][0] = max(get_item_without_null_exception(i-1, k, 0, dp), get_item_without_null_exception(i-1, k-1, 1, dp))
                dp[i][k][1] = max(get_item_without_null_exception(i-1, k, 1, dp), get_item_without_null_exception(i-1, k-1, 0, dp)) + 1
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
