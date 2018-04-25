class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if (len(M) == 0 or len(M[0]) == 0):
            return 0
        
        # Make visited array list
        visited_lst = [[False for _ in range(len(M[0]))] for _ in range(len(M))]
        def visit(i, j):
            visited_lst[i][j] = True
            visited_lst[j][i] = True

        def visited(i, j):
            if visited_lst[i][j]:
                return True
            return False

        answer = 0
        for i in range(len(M)):
            if visited(i, i): continue
            answer += 1
            visit(i, i)
            stack = [(i, j) for j in range(len(M))]
            while stack:
                cur_i, cur_j = stack.pop()
                if visited(cur_i, cur_j): continue
                if M[cur_i][cur_j] == 0: continue
                visit(cur_i, cur_j)
                for new_one in range(len(M)):	
                    stack.append((cur_j, new_one))
        
        return answer
    

solution = Solution()
test_case = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
def pprint(board):
    for each_row in board:
        print(each_row)
    print()

pprint(test_case)
print(solution.findCircleNum(test_case))
pprint(test_case)
