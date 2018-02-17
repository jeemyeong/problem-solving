def solve(n, l, puddle_list):
    end = 0
    ret = 0
    puddle_list.sort()
    for puddle_start, puddle_end in puddle_list:
        puddle_start = max(puddle_start, end)
        if puddle_start <= puddle_end:
            cnt = (puddle_end - puddle_start) // l + (1 if (puddle_end - puddle_start) % l > 0 else 0)
            ret += cnt
            end = puddle_start + cnt*l
    return ret

def run():
    import sys
    read = sys.stdin.readline

    n, l = list(map(int, read().split(" ")))
    puddle_list = []
    for i in range(n):
        puddle_list.append(list(map(int, read().split(" "))))

    print(solve(n, l, puddle_list))

run()
