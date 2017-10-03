def solve(n):
    dp = dict()
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    dp[5] = 5
    dp[6] = 6
    for i in range(6, n+1):
        dp[i] = max(dp[i-1]+1, dp[i-3]*2, dp[i-4]*3, dp[i-5]*4, dp[i-6]*5)
    return dp[n]

def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    print(solve(n))

run()
# print(solve(10))