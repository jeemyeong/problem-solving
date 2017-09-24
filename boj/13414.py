# NOT solved

def solve(K, L, students):
    last_k = set()
    q = []
    for student in students:
        q.append(student)
        if student in last_k:
            continue
        if len(last_k) < K:
            last_k.add(student)
            continue
        while len(last_k) == K:
            polled = q.pop(0)
            if polled in last_k:
                last_k.remove(polled)
        last_k.add(student)
    print(last_k)
    print(q)
    return -1

def run():
    import sys
    read = sys.stdin.readline
    K, L = map(int, read().split())
    students = []
    for _ in range(L):
        students.append(read().replace("\n", ""))
    print(solve(K, L, students))

run()
