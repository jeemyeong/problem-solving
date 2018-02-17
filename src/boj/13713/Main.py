# Not solved
import sys

def I(): return int(sys.stdin.readline())
def S(): return input()

def solve(s, i, hash_table):
    r = i; l = 0 # 길이
    ls = len(s)
    while l <= r:
        m = (l + r) // 2
        if s[i-m:i] == s[ls-m:ls]:
            l = m+1 #같으면 길이가 늘어난다.
        else:
            r = m-1 #같지 않으면 길이가 줄어든다.
    m = (l + r) // 2
    return m

def main():
    s = S()
    hash_table = {}
    for _ in range(I()):
        i = I()
        print(solve(s, i, hash_table))

main()
