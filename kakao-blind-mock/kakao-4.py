def get_element_without_null_exception(board, i, j):
    if i < 0 or j < 0:
        return 0
    else:
        return board[i][j]


def solution(board):
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(get_element_without_null_exception(dp,i-1,j-1), get_element_without_null_exception(dp,i,j-1), get_element_without_null_exception(dp,i-1,j))+1
    max_square_size = 0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j]**2 > max_square_size:
                max_square_size = dp[i][j]**2
    return max_square_size

ex_board = \
[[0, 1, 1, 1],
 [0, 1, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 1, 0]]

ex_board2 = \
[[1, 0, 1, 1],
 [1, 1, 1, 1]]
print(solution(ex_board2))
