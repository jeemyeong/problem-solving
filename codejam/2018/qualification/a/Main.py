import sys

def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())

def solve(d, p):
    length = len(p)
    list_c_idx = []
    s = 1
    damage = 0
    for i, c in enumerate(p):
        if c == "C":
            list_c_idx.append(i)
            s *= 2
        elif c == "S":
            damage += s
    if damage <= d:
        return 0
    if len(list_c_idx) == 0:
        return "IMPOSSIBLE"

    last_c_idx = max(list_c_idx)
    resolved_c_idx = len(p)
    ret = 0

    t = len(list_c_idx)
    while last_c_idx <= resolved_c_idx:
        if damage <= d:
            return ret
        if last_c_idx == resolved_c_idx-1:
            t-=1
            resolved_c_idx = last_c_idx
            list_c_idx.pop()
            if len(list_c_idx) == 0:
                return "IMPOSSIBLE"
            last_c_idx = list_c_idx[-1]
            continue
        last_c_idx += 1
        damage -= 2**(t-1)
        ret += 1
    return "IMPOSSIBLE"


def main():
    n = I()
    solutions = []
    for i in range(n):
        d, s  = LS()
        solutions.append("CASE #{}: {}".format(i+1, solve(int(d), s)))
    print("\n".join(solutions), end="")

main()
