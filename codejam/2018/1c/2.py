# Unsolved
import sys
import heapq
import collections

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())


def solve(n, lst):
    cnt = 1
    q = collections.deque([([], 0)])
    for char in lst:
        length = len(q)
        for _ in range(length):
            stack, weight = q.popleft()
            if char*6 >= weight:
                heapq.heappush(stack, -char)
                cnt = max(cnt, len(stack))
                weight += char
                q.append(([x for x in stack], weight))
                continue
            q.append(([x for x in stack], weight))
            while char*6 < weight:
                popped = heapq.heappop(stack)
                weight += popped
                q.append(([x for x in stack], weight))
            heapq.heappush(stack, -char)
            weight += char
            q.append(([x for x in stack], weight))
            
    return cnt

def main():
    t = I()
    for i in range(t):
        n = I()
        lst = LI()
        print("CASE #"+str(i+1)+":", solve(n, lst))

main()

