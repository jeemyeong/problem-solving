from collections import deque
def solution(strs, t):
    length = len(t)
    dp = dict()
    dp[''] = 0
    q = deque([''])
    while q:
        cur = q.popleft()
        for each_str in strs:
            if cur+each_str in dp:
                dp[cur+each_str] = min(dp[cur+each_str], dp[cur]+1)
            else:
                dp[cur+each_str] = dp[cur]+1
                if len(cur) + len(each_str) < length:
                    q.append(cur+each_str)
    if t in dp:
        return dp[t]
    else:
        return -1

ex_strs = ["ba", "na", "n", "a"]
ex_t = "banana"
print(solution(ex_strs,ex_t))
