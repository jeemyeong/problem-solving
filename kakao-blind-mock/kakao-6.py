def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)
    dp = [[0]*2 for _ in range(len(sticker))]
    dp[0] = [0, sticker[0]]
    dp[1] = [sticker[1], sticker[0]]
    dp[2] = [max(sticker[1], sticker[2]), (sticker[0] + sticker[2])]
    for i in range(3, len(sticker)-1):
        dp[i][0] = max(dp[i-2][0], dp[i-3][0]) + sticker[i]
        dp[i][1] = max(dp[i-2][1], dp[i-3][1]) + sticker[i]
    dp[len(sticker)-1][0] = max(dp[len(sticker)-3][0], dp[len(sticker)-4][0]) + sticker[len(sticker)-1]
    dp[len(sticker)-1][1] = max(dp[len(sticker)-3][1], dp[len(sticker)-4][1])
    return max(max(dp[len(sticker)-1]), max(dp[len(sticker)-2]))


ex_sticker_1 = [14, 6, 5, 11, 3, 9, 2, 10]
ex_sticker_2 = [1, 3, 2, 5, 4]

print(solution(ex_sticker_1))
