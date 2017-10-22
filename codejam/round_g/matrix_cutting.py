import sys
# import heapq, collections

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def solve(N, M, matrix):
    # print(matrix)
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return 0
    min_of_matrix = inf
    point_of_min = (-1, -1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if min_of_matrix > matrix[i][j]:
                point_of_min = (i, j)
                min_of_matrix = matrix[i][j]
    ret = min_of_matrix
    if len(matrix) > 1 and point_of_min[0] > 0:
        sliced_matrix1 = matrix[:point_of_min[0]]
        sliced_matrix2 = matrix[point_of_min[0]:]
        ret = max(ret, min_of_matrix + solve(N, M, sliced_matrix1) + solve(N, M, sliced_matrix2))
    if len(matrix) > 1 and point_of_min[0] < len(matrix)-1:
        sliced_matrix1 = matrix[:point_of_min[0]+1]
        sliced_matrix2 = matrix[point_of_min[0]+1:]
        ret = max(ret, min_of_matrix + solve(N, M, sliced_matrix1) + solve(N, M, sliced_matrix2))
    if len(matrix[0]) > 1 and point_of_min[1] > 0:
        sliced_matrix1 = [row[:point_of_min[1]] for row in matrix]
        sliced_matrix2 = [row[point_of_min[1]:] for row in matrix]
        ret = max(ret, min_of_matrix + solve(N, M, sliced_matrix1) + solve(N, M, sliced_matrix2))
    if len(matrix[0]) > 1 and point_of_min[1] < len(matrix[0])-1:
        sliced_matrix1 = [row[:point_of_min[1]+1] for row in matrix]
        sliced_matrix2 = [row[point_of_min[1]+1:] for row in matrix]
        ret = max(ret, min_of_matrix + solve(N, M, sliced_matrix1) + solve(N, M, sliced_matrix2))
        
    return ret

def main():
    with open("matrix_cutting.output", "w") as f:
        T = I()
        for _ in range(T):
            N, M = LI()
            matrix = [[] for _ in range(N)]
            for i in range(N):
                matrix[i] = LI()
            
            f.write(str(solve(N, M, matrix)) + "\n")

main()
