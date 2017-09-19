# Timeover

# Using buckets
def solve(n, k, values):
    buckets = [[values[i]] for i in range(n)]
    min_value = min(values)
    while True:
        bucket_index = min([j for j in range(n)], key=lambda i: buckets[i][0])
        min_value = buckets[bucket_index].pop(0)
        if min_value == k:
            break
        for j in range(n):
            if j < bucket_index:
                continue
            buckets[j].append(min_value+values[j])

    ret = 1
    for bucket in buckets:
        ret += bucket.count(k)
    return ret

def run():
    import sys
    read = sys.stdin.readline
    n, k = map(int, read().split())
    values = [-1] * n
    for i in range(n):
        values[i] = int(read())
    print(solve(n, k, values))

run()
