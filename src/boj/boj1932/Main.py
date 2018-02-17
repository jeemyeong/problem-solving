def get_element(_list, i, j):
    if i < 0 or j < 0:
        return 0
    else:
        return _list[i][j]

def run():
    import sys
    read = sys.stdin.readline

    cnt = int(read())
    _map = [[0]*(cnt) for _ in range(cnt)]
    _sum = [[0]*(cnt) for _ in range(cnt)]

    for i in range(cnt):
        line = read().replace("\n", "")
        if line[-1] == " ":
            line = line[:-1]
        _map[i] = list(map(int, line.split(" ")))

    for i in range(cnt):
        for j in range(i+1):
            _sum[i][j] = max(get_element(_sum, i-1, j-1), get_element(_sum, i-1, j)) + _map[i][j]

    print(max(_sum[cnt-1]))

run()
