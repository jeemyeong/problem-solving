# Not solved
def solve(T, W, order):
    from collections import deque
    q = deque([])
    q.append((0, 1, W, 1 if 1 == order[0] else 0))
    q.append((0, 2, W, 1 if 2 == order[0] else 0))
    ret = 0
    while q:
        index, position, left_w, count = q.popleft()
        if count > ret:
            ret = count
        if index == T-1:
            continue
        if position == 1:
            q.append((index+1, 1, left_w, count + (1 if order[index+1] == 1 else 0)))
            if left_w > 0:
                q.append((index+1, 2, left_w-1, count + (1 if order[index+1] == 2 else 0)))
        if position == 2:
            q.append((index+1, 2, left_w, count + (1 if order[index+1] == 2 else 0)))
            if left_w > 0:
                q.append((index+1, 1, left_w-1, count + (1 if order[index+1] == 1 else 0)))
    return ret

def run():
    import sys
    read = sys.stdin.readline
    T, W = map(int, read().split())
    order = []
    for _ in range(T):
        order.append(int(read()))
    print(solve(T, W, order))

run()
