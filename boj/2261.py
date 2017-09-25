def dist(point1, point2):
    return (point1[0]-point2[0]) ** 2 + (point1[1]-point2[1]) ** 2 

def recursive_solve(points, start, end):
    if start == end:
        INF = 1e100
        return INF
    mid = (start+end)//2
    d = min(recursive_solve(points, start, mid), recursive_solve(points, mid +1, end))
    i = mid
    while i <= end and (points[mid][0] - points[i][0])**2<d:
        i += 1
    j = mid
    while j >= start and (points[mid][0] - points[j][0])**2 < d:
        j -= 1
    center = sorted(points[j+1:i], key=lambda x : x[1])
    for i in range(len(center)-1):
        for j in range(i+1, i+7):
            if j >= len(center):
                break
            if center[j][1] - center[j][1] >= d:
                break
            d = min(d, dist(center[i], center[j]))
    return d

def solve(n, points):
    points.sort(key=lambda x: x[0])
    return recursive_solve(points, 0, n-1)


def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    points = []
    for _ in range(n):
        points.append(list(map(int, read().replace("\n", "").split())))
    print(solve(n, points))

run()
