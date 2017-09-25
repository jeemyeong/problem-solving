def solve(n, meetings):
    meeting_sorted_by_end = dict([(meetings[i][1], []) for i in range(n)])
    for start, end in meetings:
        meeting_sorted_by_end[end].append(start)
    dp = [0] * (max(meeting_sorted_by_end) + 1)
    for i, count in enumerate(dp):
        if i != 0:
            dp[i] = dp[i-1]
        if not i in meeting_sorted_by_end:
            continue
        same_start_and_end = 0
        for start in meeting_sorted_by_end[i]:
            if start == i:
                same_start_and_end += 1
                continue
            dp[i] = max(dp[i], dp[start] + 1)
        if same_start_and_end:
            dp[i] += same_start_and_end
    return dp[-1]

def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    meetings = []
    for _ in range(n):
        meetings.append(list(map(int, read().replace("\n", "").split())))
    print(solve(n, meetings))

run()
