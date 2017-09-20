def solve(N, stickers):
    dp = [[0]*N for _ in range(3)]
    dp[1][0] = stickers[0][0]
    dp[2][0] = stickers[1][0]
    for j in range(1, N):
        dp[0][j] = max(dp[1][j-1], dp[2][j-1])
        dp[1][j] = max(dp[0][j-1] + stickers[0][j], dp[2][j-1] + stickers[0][j])
        dp[2][j] = max(dp[0][j-1] + stickers[1][j], dp[1][j-1] + stickers[1][j])
    return max([dp[0][N-1], dp[1][N-1], dp[2][N-1]])

def run():
    import sys
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        N = int(read())
        stickers = []
        for _ in range(2):
            row = list(map(int, read().split()))
            stickers.append(row)
        print(solve(N, stickers))

run()
