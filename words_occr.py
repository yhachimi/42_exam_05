class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True 

            c = word[index]
            if row < 0 or row >= rows or col < 0 or col >= cols or  board[row][col] != c:
                return False
            tmp = board[row][col]
            board[row][col] = "#"

            found = (dfs(row, col + 1, index + 1)
            or dfs(row + 1, col, index + 1)
            or dfs(row, col - 1, index + 1)
            or dfs(row - 1, col, index + 1))

            board[row][col] = tmp
            return found



        for r in range(rows):
            for c  in range(cols):
                if dfs(r, c, 0):
                    return True 


        return False
            



        
            

