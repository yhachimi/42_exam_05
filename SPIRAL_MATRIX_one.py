class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        top = 0

        res = []


        while top <= bottom and left <= right:

        # right side
            for col  in range(left, right + 1):
                res.append(matrix[top][col])

            top += 1


            # down
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])

            right -= 1



         #left side 
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])

                bottom -= 1 


        # up  side 
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
            
                left += 1


        return res
   
