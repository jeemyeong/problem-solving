def count_upward_same_color_in_col_at_position(y, x, board, color):
    cnt = 0
    for i in range(y-1, -1, -1):
        if board[i][x] == color:
            cnt += 1
        else:
            break
    return cnt

def count_downward_same_color_in_col_at_position(y, x, board, color):
    cnt = 0
    for i in range(y+1, len(board)):
        if board[i][x] == color:
            cnt += 1
        else:
            break
    return cnt

def count_leftward_same_color_in_row_at_position(y, x, board, color):
    cnt = 0
    for i in range(x-1, -1, -1):
        if board[y][i] == color:
            cnt += 1
        else:
            break
    return cnt

def count_rightward_same_color_in_row_at_position(y, x, board, color):
    cnt = 0
    for i in range(x+1, len(board[0])):
        if board[y][i] == color:
            cnt += 1
        else:
            break
    return cnt

def count_same_color_in_col_at_position(y, x, board, color):
    cnt = 1
    cnt += count_upward_same_color_in_col_at_position(y, x, board, color)
    cnt += count_downward_same_color_in_col_at_position(y, x, board, color)
    return cnt

def count_same_color_in_row_at_position(y, x, board, color):
    cnt = 1
    cnt += count_leftward_same_color_in_row_at_position(y, x, board, color)
    cnt += count_rightward_same_color_in_row_at_position(y, x, board, color)
    return cnt

def solve(N, board):
    q = [[i, j] for i in range(N) for j in range(N)]
    ret = 0
    for y, x in q:
        ret = max(ret, count_same_color_in_col_at_position(y, x, board, board[y][x]))
        if x >= 1:
            ret = max(ret, count_same_color_in_col_at_position(y, x, board, board[y][x-1]))
            ret = max(ret, count_rightward_same_color_in_row_at_position(y, x, board, board[y][x-1])+1)
        if x < N-1:
            ret = max(ret, count_same_color_in_col_at_position(y, x, board, board[y][x+1]))
            ret = max(ret, count_leftward_same_color_in_row_at_position(y, x, board, board[y][x+1])+1)

        ret = max(ret, count_same_color_in_row_at_position(y, x, board, board[y][x]))
        if y >= 1:
            ret = max(ret, count_same_color_in_row_at_position(y, x, board, board[y-1][x]))
            ret = max(ret, count_downward_same_color_in_col_at_position(y, x, board, board[y-1][x])+1)
        if y < N-1:
            ret = max(ret, count_same_color_in_row_at_position(y, x, board, board[y+1][x]))
            ret = max(ret, count_upward_same_color_in_col_at_position(y, x, board, board[y+1][x])+1)
    return ret

def run():
    import sys
    read = sys.stdin.readline
    N = int(read())
    board = []
    for _ in range(N):
        board.append(read().replace("\n", ""))
    print(solve(N, board))

run()
