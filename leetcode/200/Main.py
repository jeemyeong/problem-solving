class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        cols = len(grid)
        rows = len(grid[0])
        visited = [[False for _ in range(rows)] for _ in range(cols)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ret = 0
        def is_valid_position(y, x):
            return not (y < 0 or x < 0 or y >= cols or x >= rows)
        
        def union_find(y, x):
            if grid[y][x] == "0" or visited[y][x]:
                return 0
            stack = [(y, x)]
            while stack:
                (cur_y, cur_x) = stack.pop()
                if visited[cur_y][cur_x]:
                    continue
                visited[cur_y][cur_x] = True
                for direction in directions:
                    new_y = cur_y + direction[0]
                    new_x = cur_x + direction[1]
                    if is_valid_position(new_y, new_x) and grid[new_y][new_x] == grid[cur_y][cur_x]:
                        stack.append((new_y, new_x))
            return 1
        
        ret = 0
        for y in range(cols):
            for x in range(rows):
                ret += union_find(y, x)
        return ret
        

solution = Solution()
test_case = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
def pprint(board):
    for each_row in board:
        print(each_row)
    print()

# pprint(test_case)
print(solution.numIslands(test_case))
