import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())

def solve(n, lst):
    lst_a = []
    lst_b = []
    for i, e in enumerate(lst):
        if i % 2 == 0:
            lst_a.append(e)
        else:
            lst_b.append(e)
    sorted_lst = []
    lst_a.sort()
    lst_b.sort()
    half_n = n // 2
    for i in range(half_n):
        sorted_lst.append(lst_a[i])
        sorted_lst.append(lst_b[i])
    if len(lst_a) > len(lst_b):
        sorted_lst.append(lst_a[-1])
    for i in range(n-1):
        if sorted_lst[i] > sorted_lst[i+1]:
            return i
    return "OK"

def main():
    t = I()
    solutions = []
    for i in range(t):
        n = I()
        lst = LI()
        solutions.append("CASE #{}: {}".format(i+1, solve(n, lst)))
    print("\n".join(solutions), end="")


main()
