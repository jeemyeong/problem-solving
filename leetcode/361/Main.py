class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        EMPTY = "0"
        ENEMY = "E"
        WALL = "W"
        def is_empty(cell):
            return EMPTY == cell
        def is_enemy(cell):
            return ENEMY == cell
        def is_wall(cell):
            return WALL == cell

        kill = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(0, rows):
            cnt = 0
            for col in range(0, cols):    
                cell = grid[row][col]
                if is_enemy(cell): cnt+=1
                elif is_empty(cell): kill[row][col] += cnt
                elif is_wall(cell): cnt = 0

        for row in range(0, rows):
            cnt = 0
            for col in range(cols-1, -1, -1):
                cell = grid[row][col]
                if is_enemy(cell): cnt+=1
                elif is_empty(cell): kill[row][col] += cnt
                elif is_wall(cell): cnt = 0
                
        for col in range(0, cols):
            cnt = 0
            for row in range(0, rows):
                cell = grid[row][col]
                if is_enemy(cell): cnt+=1
                elif is_empty(cell): kill[row][col] += cnt
                elif is_wall(cell): cnt = 0

        for col in range(0, cols):
            cnt = 0
            for row in range(rows-1, -1, -1):
                cell = grid[row][col]
                if is_enemy(cell): cnt+=1
                elif is_empty(cell): kill[row][col] += cnt
                elif is_wall(cell): cnt = 0
        return max(sum(kill, []))
        
print(Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))