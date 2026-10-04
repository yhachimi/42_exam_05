def word_serach(chrs, tar_word) -> list[dict]:




    dirctions = [

            ("left-to-right", (0, 1)), 
            ("right-to-left", (0, -1)), 
            ( "top-to-bottom", (1, 0)),
            ( "bottom-to-top", (-1, 0)), 
             ("top-left", (-1, -1)),
             ("top-right", (-1, 1)),
             ("bottom-left", (1, -1)),
             ("bottom-right", (1,1))
            ]




    res = []

    i = 0
    hight = len(chrs)
    width = len(chrs[0])
    for row in range(hight):
        for col in range(width):
            for dirc, moves in dirctions:
                x, y = moves 
                for i in range(len(tar_word)):
                    dx = row + x * i
                    dy = col + y * i
                    if dx < 0 or dx >= hight or dy < 0 or dy >= width or tar_word[i] != chrs[dx][dy]:
                          break

                else: 
                    res.append({"dirction": dirc, "pos": (row, col)})








    return res



board = [
    ["A","B","C","D"],
    ["S","B","B","S"],
    ["A","D","C","A"],
    ["B","E","D","D"]
]

print(word_serach(board, "ABCD"))



