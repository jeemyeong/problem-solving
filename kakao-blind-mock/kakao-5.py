def max_from_different_col(land, i, j):
    elements_from_dirfferent_col = []
    for dj in [0, 1, 2, 3]:
        if j == dj:
            continue
        elements_from_dirfferent_col.append(land[i-1][dj])
    return max(elements_from_dirfferent_col)

def solution(land):
    max_land = [[0]*4 for _ in range(len(land))]
    max_land[0] = [land[0][x] for x in range(4)]
    for i in range(1, len(land)):
        for j in range(4):
            max_land[i][j] = max_from_different_col(max_land, i, j) + land[i][j]
    return max(max_land[len(land)-1])

ex_land = \
[[1, 2, 3, 5],
 [5, 6, 7, 8],
 [5, 6, 7, 8],
 [5, 6, 7, 8],
 [4, 3, 2, 1]]

print(solution(ex_land))
