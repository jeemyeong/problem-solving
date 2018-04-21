class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        cols = len(board)
        rows = len(board[0])
        def check_exception(y, x):
            return y < 0 or x < 0 or y >= cols or x >= rows
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Check group is surrounded by "X"
        def is_surrounded_by_X(board, visited, y, x):
            if visited[y][x]:
                return board[y][x] == "X"
            visited_in_stack = [[False for row in range(rows)] for col in range(cols)]
            stack = [(y,x)]
            while stack:
                y, x = stack.pop()
                if visited[y][x]:
                    if board[y][x] == "O":
                        return False
                    continue
                if visited_in_stack[y][x]:
                    continue
                visited_in_stack[y][x] = True
                if board[y][x] == "X":
                    continue
                for direction in directions:
                    new_y = y + direction[0]
                    new_x = x + direction[1]
                    if check_exception(new_y, new_x):
                        return False
                    stack.append((new_y, new_x))
            visited[y][x] = True
            return True
        
        def convert_to_X(board, y, x):
            stack = [(y,x)]
            while stack:
                y,x = stack.pop()
                if board[y][x] == "X":
                    continue
                board[y][x] = "X"
                for direction in directions:
                    new_y = y + direction[0]
                    new_x = x + direction[1]
                    if check_exception(new_y, new_x):
                        return
                    stack.append((new_y, new_x))
            return

        visited = [[False for row in range(rows)] for col in range(cols)]
        for col in range(cols):
            for row in range(rows):
                if board[col][row] == "O" and is_surrounded_by_X(board, visited, col, row):
                    convert_to_X(board, col, row)


solution = Solution()
test_case = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
def pprint(board):
    for each_row in board:
        print(each_row)
    print()

pprint(test_case)
solution.solve(test_case)
pprint(test_case)
