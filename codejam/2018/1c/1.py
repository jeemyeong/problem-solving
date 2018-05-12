import sys
import collections


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def S(): return input()

def solve(n, l, lst):
    if l == 1:
        return "-"

    lines = []
    _set = set()
    for i in range(l):
        for string in lst:
            _set.add(string[:i+1])
        lines.append(set(map(lambda x: x[i], lst)))
    queue = collections.deque()
    
    for char in lines[0]:
        queue.append((char, 1))

    while len(queue) > 0:
        cur, length = queue.pop()
        if length == l:
            return cur
        for char in lines[length]:
            _next = cur+char
            if not char in cur and not _next in _set:
                queue.appendleft((_next, length + 1))

    return "-"

def main():
    t = I()
    for i in range(t):
        lst = []
        n, l = LI()
        for _ in range(n):
            lst.append(S())
        print("CASE #"+str(i+1)+":", solve(n, l, lst))

main()

