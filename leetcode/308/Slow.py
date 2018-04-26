class NumMatrix:
  
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = 0 if len(matrix) == 0 else len(matrix[0])

    def is_valid(self, row, col):
        return 0 <= row and 0 <= col and row < self.rows and col < self.cols

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if not self.is_valid(row, col):
            return
        self.matrix[row][col] = val
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        row1 = max(0, row1)
        row2 = min(self.rows-1, row2)
        col1 = max(0, col1)
        col2 = min(self.cols-1, col2)
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                ret += self.matrix[row][col]
        return ret
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
obj = NumMatrix(matrix)
print(obj.sumRegion(2,1,4,3))
obj.update(3,2,2)
print(obj.sumRegion(2,1,4,3))