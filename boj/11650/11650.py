import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(points):
    points.sort(key= lambda point: point["y"])
    points.sort(key= lambda point: point["x"])
    ret = "\n".join(["%s %s" % (point["x"], point["y"]) for point in points])
    return ret

def main():
    N = I()
    points = []
    for _ in range(N):
        x, y = LI()
        point = {
            "x" : x,
            "y" : y
        }
        points.append(point)
    print(solve(points))

main()
