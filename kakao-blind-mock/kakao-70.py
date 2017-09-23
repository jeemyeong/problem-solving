def dfs(strs, t, dp):
    if t in dp:
        return dp[t]
    if len(t) == 0 or len(strs) == 0:
        dp[t] = 0
        return dp[t]
    min_solution = 10e100
    new_strs = set(x for x in strs)
    for each_str in strs:
        if t.count(each_str) == 0:
            new_strs.remove(each_str)
    for each_str in new_strs:
        if t[:len(each_str)] == each_str:
            sol = dfs(new_strs, t[len(each_str):], dp)
            if sol != -1:
                min_solution = min(min_solution, sol)
    if min_solution != 10e100:
        dp[t] = min_solution +1
    else:
        dp[t] = -1
    return dp[t]

def solution(strs, t):
    dp = dict()
    return dfs(set(strs), t, dp)

ex_strs = ["ba", "na", "n", "a"]
ex_t = "banana"
print(solution(ex_strs,ex_t))
