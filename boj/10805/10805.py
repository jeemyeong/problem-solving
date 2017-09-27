# Not solved

def solve(h1, w1, h2, w2):
    w3 = w1-w2
    h3 = h1-h2
    return -1

def run():
    import sys
    read = sys.stdin.readline
    h1, w1, h2, w2 = list(map(int, read().replace("\n", "").split()))
    print(solve(h1, w1, h2, w2))

run()
