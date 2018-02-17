def rect(h, w, rect_dict):
    if (h, w) in rect_dict:
        return rect_dict[(h, w)]
    ret = 0
    if h > w:
        ret = h//w
        ret += rect(h%w, w, rect_dict)
    rect_dict[(h,w)] = ret
    rect_dict[(w,h)] = ret
    return ret

def solve(h1, w1, h2, w2):
    INF = 1e100
    dp = [[[[INF]*51 for _ in range(51)] for _ in range(51)] for _ in range(51)]
    rect_dict = dict()
    for y in range(1, 51):
        for x in range(1, 51):
            if y == x:
                dp[y][x][0][0] = 1
            else:
                dp[y][x][0][0] = INF
            for i in range(1, y):
                dp[y][x][0][0] = min(dp[y][x][0][0], dp[i][x][0][0] + dp[y-i][x][0][0])
            for j in range(1, x):
                dp[y][x][0][0] = min(dp[y][x][0][0], dp[y][j][0][0] + dp[y][x-j][0][0])
    for y in range(1, h1+1):
        for x in range(1, w1+1):
            for i in range(1, y):
                for j in range(1, x):
                    dp[y][x][i][j] = INF
                    for k in range(1, x-j):
                        dp[y][x][i][j] = min(dp[y][x][i][j], dp[y][k][0][0] + dp[y][x-k][i][j])
                    dp[y][x][i][j] = min(dp[y][x][i][j], dp[y][x-j][0][0] + dp[y-i][j][0][0])
                    for k in range(x-j+1, x):
                        dp[y][x][i][j] = min(dp[y][x][i][j], dp[y][k][i][k-(x-j)] + dp[y-i][x-k][0][0])
                    for k in range(1, i):
                        dp[y][x][i][j] = min(dp[y][x][i][j], dp[k][x-j][0][0] + dp[y-k][x][i-k][j])
                    dp[y][x][i][j] = min(dp[y][x][i][j], dp[i][x-j][0][0] + dp[y-i][x][0][0])
                    for k in range(i+1, y):
                        dp[y][x][i][j] = min(dp[y][x][i][j], dp[k][x][i][j] + dp[y-k][x][0][0])
    return dp[h1][w1][h2][w2]

def run():
    import sys
    read = sys.stdin.readline
    h1, w1, h2, w2 = list(map(int, read().replace("\n", "").split()))
    print(solve(h1, w1, h2, w2))

run()
