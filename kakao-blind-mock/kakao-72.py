import sys
sys.setrecursionlimit(25000)

MAX_INT = 1e100
def solve(visit, t, idx, dp):
    if idx in dp:
        return dp[idx]
    dp[idx] = MAX_INT
    for n in range(idx, min(idx+5, len(t))):
        if t[idx:n+1] in visit:
            dp[idx] = min(dp[idx], solve(visit, t, n+1, dp)+1)
    return dp[idx]

def solution(strs, t):
    dp = dict()
    dp[len(t)] = 0
    ret = solve(set(strs), t, 0, dp)
    if ret >= MAX_INT:
        return -1
    return ret

print(solution(["banan", "n", "a"],"banana")==2)
print(solution(["ba", "na", "n", "a"],"banana")==3)
print(solution(["ba", "na", "n", "b"],"b")==1)
print(solution(["app","ap","p","l","e","ple","pp"],"apple")==2)
print(solution(["ba","an","nan","ban","n"],"banana")== -1)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def test_runtime_error():
    import random
    c = random.randint(1, 5)
    ex_strs = []
    for _ in range(100):
        ex_str = ''
        for i in range(random.randint(1,5)):
            ex_str += random.choice(alphabet)
        ex_strs.append(ex_str)
    ex_t = ''
    for _ in range(20000):
        ex_t += random.choice(alphabet)
    return solution(ex_strs, ex_t)

for _ in range(100):
    ret = test_runtime_error()
    if ret == -1:
        print("Hello")
