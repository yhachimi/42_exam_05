class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]

        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        num = 1
        while left <= right and top <= bottom:

            # right
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1

            # down
            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1

            right -= 1

            # left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1

                bottom -= 1

            # up
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1

                left += 1

        return res


sol = Solution()

print(sol.generateMatrix(3))
