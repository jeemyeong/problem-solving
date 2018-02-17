def count_two_in_num(num):
    ret = 0
    while num > 0:
        ret += num//2
        num //= 2
    return ret

def count_five_in_num(num):
    ret = 0
    while num > 0:
        ret += num//5
        num //= 5
    return ret

def solve(n, m):
    l = n - m
    count_five = count_five_in_num(n) - count_five_in_num(m) - count_five_in_num(l)
    count_two = count_two_in_num(n) - count_two_in_num(m) - count_two_in_num(l)
    return min(count_five, count_two)

def run():
    import sys
    read = sys.stdin.readline

    n, m = list(map(int, read().split()))
    print(solve(n, m))

run()
# print(solve(25, 12))
