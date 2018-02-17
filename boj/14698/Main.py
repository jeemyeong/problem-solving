import heapq
def solve(N, slimes): # Using heap, 1636 MS	is used
    if N == 1:
        return 1
    ret = 1
    heap_slimes = []
    for slime in slimes:
        heapq.heappush(heap_slimes, (slime, slime))
    for _ in range(N-1):
        first_min = heapq.heappop(heap_slimes)
        second_min = heapq.heappop(heap_slimes)
        new_slime = first_min[1] * second_min[1]
        heapq.heappush(heap_slimes, (new_slime, new_slime))
        slimes.append(new_slime)
        ret *= new_slime
    return ret % 1000000007

def solve2(N, slimes): # Using min, 2108 MS	is used
    if N == 1:
        return 1
    ret = 1
    for _ in range(N-1):
        first_min = slimes.pop(slimes.index(min(slimes)))
        second_min = slimes.pop(slimes.index(min(slimes)))
        new_slime = first_min * second_min
        slimes.append(new_slime)
        ret *= new_slime
    return ret % 1000000007


def run():
    import sys
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        N = int(read())
        slimes = [int(i) for i in read().split()]
        print(solve(N, slimes))

run()
