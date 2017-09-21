MAX_INT = 1e100
def solution(strs, t):
    set_strs = set(strs)
    dp = [MAX_INT] * (len(t)+1)
    dp[0] = 0
    for j in range(1, len(t)+1):
        dp[j] = MAX_INT
        for i in range(1, 6):
            if (j-i) < 0:
                continue
            if t[j-i:j] in set_strs:
                dp[j] = min(dp[j], dp[j-i]+1)
    ret = dp[len(t)]
    if ret == MAX_INT:
        return -1
    return ret

print(solution(["banan", "n", "a"],"banana")==2)
print(solution(["ba", "na", "n", "a"],"banana")==3)
print(solution(["ba", "na", "n", "b"],"b")==1)
print(solution(["app","ap","p","l","e","ple","pp"],"apple")==2)
print(solution(["ba","an","nan","ban","n"],"banana")== -1)