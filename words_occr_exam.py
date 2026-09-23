class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: list[dict]
        """
        rows = len(board)
        cols = len(board[0])


        res = []
        
        directions = [
            (-1, -1, "top-left"),
            (-1,  0, "top"),
            (-1,  1, "top-right"),
            ( 0, -1, "left"),
            ( 0,  1, "right"),
            ( 1, -1, "bottom-left"),
            ( 1,  0, "bottom"),
            ( 1,  1, "bottom-right")
        ]
        





        for r in range(rows):
            for c in range(cols):
                for dr, dc, name  in directions:
                    for i in range(len(word)):
                        nr = r  + dr * i
                        nc = c + dc * i

                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != word[i]:
                            break

                    else:
                        res.append({"directions": (name), "pos": (r, c)})


        return res



s = Solution()





board = [
    ["A","C","C","D"],
    ["S","B","B","S"],
    ["A","D","C","A"],
    ["B","E","D","D"]
]

print(s.exist(board, "ABCD"))
