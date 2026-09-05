def matrix_sprial(n: int):
    res = [[0] * n for _ in range(n)]

    bottom = n - 1
    left = 0 
    right = n - 1
    top = 0 
    num = 1


    while top <= bottom and left <= right:

        # right side 
        for col  in range(left, right + 1):
            res[top][col] = num 
            num += 1 

        top += 1


        # down
        for row in range(top, bottom + 1):
            res[row][right] = num 
            num += 1 

        right -= 1



        #left side 

        for col in range(right, left - 1, -1):
            res[bottom][col] = num 
            num += 1

        bottom -= 1 


        # up  side 
        for row in range(bottom, top - 1, -1):
            res[row][left] = num
            num  += 1 
        left += 1



    print(res)
    return res 





matrix_sprial(3)
