def solve(string, k):
    queue = [None] * k
    cur = ""
    strings = []
    for i, c in enumerate(string):
        cur += c
        if c in queue:
            queue.pop(queue.index(c))
            queue.append(c)
            continue
        elif c not in queue:
            strings.append(cur)
            deleted = queue.pop(0)
            queue.append(c)
            if deleted is None:
                continue
            while deleted in cur:
                cur = cur[cur.index(deleted)+1:]
    strings.append(cur)
    return max(strings, key=lambda x: len(x))

print(solve("abcccccbbbbbdddddcccddddaa", 3))