def solve(n, password):
    check = dict()
    for p in password:
        if p in check:
            check[p] += 1
        else:
            check[p] = 1
        reverse_p = ''.join(reversed(list(p)))
        if reverse_p in check:
            check[reverse_p] += 1
        else:
            check[reverse_p] = 1
    for p in check:
        if check[p] == 2:
            return str(len(p)) + " " + p[len(p)//2]

def run():
    import sys
    read = sys.stdin.readline
    n = int(read().replace("\n", ""))
    password = []
    for _ in range(n):
        password.append(read().replace("\n", ""))
    print(solve(n, password))

run()
