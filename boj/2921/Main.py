def solve(n):
    return int((n+2)*n*(n+1)/2)

def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    print(solve(n))

run()
