import sys
# import heapq, collections

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

def solve(n, seq):
    valid = []
    not_valid = []
    for i in range(n):
        if len(valid) == 0 or seq[i] < seq[valid[-1]]:
            valid.append(i)
        else:
            not_valid.append(i)
    res = 0
    n = len(valid)-1
    for j in range(len(not_valid)-1, -1, -1):
        end_point = not_valid[j]
        if n < 0:
            break
        start_point = valid[n]
        while 0 <= n and seq[start_point] <= seq[end_point] and start_point < end_point:
            res = max(res, end_point - start_point)
            n-=1
            start_point = valid[n]
    return res

# def solve(n, seq):
#     ans = 0
#     for i in range(n-1, 0, -1):
#         for j in range(0, n-i):
#             if seq[j] <= seq[j+i]:
#                 return i
#     return ans

    


def main():
    t = I()
    for _ in range(t):
        n = I()
        seq = LI()
        print(solve(n, seq))

main()
