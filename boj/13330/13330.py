def solve(n, k, l, w, dp):
    INF = 1e100
    if w in dp:
        return dp[w]
    u = 0
    for i in range(n//2):
        if w[i] == w[n-i-1]:
            u += 1
        else:
            break
    if n * k <= 2 * u * l:
        dp[w] = 1
        return 1
    ret = INF
    for i in range(2, n-1):
        if solve(i, k, l, w[:i], dp) != 0 and solve(n-i, k, l, w[i:], dp) != 0:
            ret = min(ret, solve(i, k, l, w[:i], dp) + solve(n-i, k, l, w[i:], dp))
    if ret == INF:
        dp[w] = 0
        return 0
    dp[w] = ret
    return ret

def run():
    import sys
    read = sys.stdin.readline
    n, k, l = map(int, read().split())
    w = read()
    dp = dict()
    print(solve(n, k, l, w, dp))

run()