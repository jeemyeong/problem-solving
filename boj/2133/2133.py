def solve(n):
    if n%2 == 1:
        return 0
    dp = dict()
    dp[0] = 1
    dp[2] = 3
    for i in range(4,31,2):
        dp[i] = dp[i-2] * 3
        for j in range(0, i-2, 2):
            dp[i] += dp[j] * 2
    return dp[n]

def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    print(solve(n))

run()
# print(solve(2))