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

def solve(string):
    stack = []
    for i, e in enumerate(string):
        if e == "(":
            stack.append(i)
        elif e == ")" and len(stack) > 1:
            j = stack.pop()
        elif e == ")" and len(stack) == 1:
            j = stack.pop()
            front = string[:j]
            middles = solve(string[j+1:i])
            backs = solve(string[i+1:])
            ret = set()
            for middle in middles:
                for back in backs:
                    ret.add(front+"("+middle+")"+back)
                    ret.add(front+middle+back)
            return ret     
    return set([string])

def main():
    string = S()
    ret = solve(string)
    ret.remove(string)
    print("\n".join(sorted(ret)))

main()
