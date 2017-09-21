def solve(n, k, values):
    cache = [0]*(k+1)
    cache[0] = 1
    for value in values:
        for i in range(k+1):
            if i >= value:
                cache[i] += cache[i-value]
    return cache[k]

def run():
    import sys
    read = sys.stdin.readline
    n, k = map(int, read().split())
    values = [-1] * n
    for i in range(n):
        values[i] = int(read())
    print(solve(n, k, values))

run()
