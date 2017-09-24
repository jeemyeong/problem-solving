def pprint(dp):
    for i in dp:
        print(i)
    print()

def solve(K, files):
    sizes = [0]
    for i in range(K):
        sizes.append(sizes[i]+files[i])
    INF = 1e100
    dp = [[INF] * K for _ in range(K)]
    for i in range(K-1):
        dp[i][i] = 0
        dp[i][i+1] = files[i] + files[i+1]
    dp[K-1][K-1] = 0
    for i in range(K-3, -1, -1):
        for j in range(i+2, K):
            dp[i][j] = INF
            size = sizes[j+1] - sizes[i]
            # size = sum(files[i:j+1])
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + size)
    return dp[0][K-1]

def run():
    import sys
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        K = int(read())
        files = list(map(int, read().split()))
        print(solve(K, files))

run()
