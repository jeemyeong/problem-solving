# Not solved

def solve(m, lines):
    print(lines)
    return -1

def run():
    import sys
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        m = int(read())
        lines = []
        for _ in range(m):
            line = list(map(int, read().split()))
            points = []
            for i in range(line.pop(0)):
                x = line.pop(0)
                y = line.pop(0)
                points.append((x, y))
            lines.append(points)
        print(solve(m, lines))

run()
