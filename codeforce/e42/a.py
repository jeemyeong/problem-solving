import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(n, lst):
    t = (sum(lst)+1)//2
    for i, e in enumerate(lst):
        t -= e
        if t <= 0:
          return i+1
    return -1

def main():
    n = I()
    lst = LI()
    print(solve(n, lst))

main()
