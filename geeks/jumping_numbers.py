import sys, collections
# import heapq

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def check_jumping_number(n):
    n = list(map(int, list(str(n))))
    for i in range(1, len(n)):
        if n[i-1] != n[i]-1 and n[i-1] != n[i]+1:
            return False
    return True

def get_pow(n):
    p = 0
    while n >= 10:
        n//=10
        p+=1
    return p    

def solve(n):
    p = get_pow(n)
    nums = '0123456789'
    ret = set()
    q = collections.deque(list(nums))
    while q:
        cur = q.popleft()
        if int(cur) > n:
            continue
        ret.add(int(cur))
        if int(cur[-1]) + 1 <= 9:
            q.append(cur + str(int(cur[-1]) + 1))
        if int(cur[-1]) - 1 >= 0:
            q.append(cur + str(int(cur[-1]) - 1))
    return ret
        
def main():
    t = I()
    for _ in range(t):
        n = I()
        print(' '.join(sorted(map(str, solve(n)))))

main()
