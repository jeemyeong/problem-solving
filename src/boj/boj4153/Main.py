import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]

def solve(x,y,z):
    a,b,c = sorted([x**2,y**2,z**2])
    if a+b == c:
        return "right"
    return "wrong"

def main():
    x,y,z = LI()
    while (x,y,z) != (0,0,0):
        print(solve(x,y,z))
        x,y,z = LI()

main()
