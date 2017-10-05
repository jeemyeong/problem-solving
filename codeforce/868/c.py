import sys
read = sys.stdin.readline

def solve(n, k, data):
    dataset = set()
    for d in data:
        dataset.add(d)
    for i in dataset:
        for j in dataset:
            matched = False
            for e in range(k):
                if i[e] == j[e]:
                    matched = True
                    break
            if not matched:
                return "YES"
    return "NO"

def run():
    n, k = list(map(int, read().replace("\n", "").split()))
    data = []
    for i in range(n):
        data.append("".join(read().replace("\n", "").split()))
    print(solve(n, k, data))

run()