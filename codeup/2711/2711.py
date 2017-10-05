import sys
read = sys.stdin.readline

def solve(n, exp, money):
    sortedList = sorted(range(n), key=lambda x: money[x]/exp[x])
    e = 1
    ret = 0
    for t in sortedList:
        ret += e*money[t]
        e += e*exp[t]
    return ret % 1000000000

def run():
    n = int(read().replace("\r\n", "").replace("\n", ""))
    exp = list(map(int, filter(lambda x: x != '', read().replace("\r\n", "").replace("\n", "").split(" "))))
    money = list(map(int, filter(lambda x: x != '', read().replace("\r\n", "").replace("\n", "").split(" "))))
    print(solve(n, exp, money))

run()