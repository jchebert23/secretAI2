#!/usr/bin/python

def stability(board, color):
    myVal = 0
    oppVal = 0
    i =0
    corners = [[0,0],[0,7],[7,7],[7,0]]
    for corner in corners:
        if(i<2):
            increment = 1
        else:
            increment = -1
        xCorn = corner[0]
        yCorn = corner[1]
        curColor = board[xCorn][yCorn]
        stableChain = 0
        stableCorner = 0
        tentChain = 0
        if(curColor != 0):
            stableCorner = 1
        for w in range(7):
            if(board[xCorn][yCorn] == curColor and curColor != 0):
                if(stableCorner):
                    print("Adding to stable chain")
                    stableChain += 1
                else:
                    tentChain += 1
            else:
                stableCorner = 0
                if(stableChain != 0):
                    if(curColor == color):
                        myVal += stableChain
                    else:
                        oppVal += stableChain
                stableChain = 0
                curColor = board[xCorn][yCorn]
                if(curColor!= 0):
                    tentChain = 1
            print("X: ", xCorn, "Y: ", yCorn, " Val: ", board[xCorn][yCorn])
            if(i % 2 == 0):
                yCorn += increment
            else:
                xCorn += increment
        if(i < 3):
            newX = corners[i+1][0]
            newY = corners[i+1][1]
        else:
            newX = 0
            newY = 0
        if(tentChain != 0 and board[newX][newY] == curColor):
            if(curColor == color):
                myVal += tentChain
            else:
                oppVal += tentChain
        
        if(stableChain != 0 and board[newX][newY] == curColor):
            if(curColor == color):
                myVal += stableChain
            else:
                oppVal += stableChain
        
        
        i += 1
    print("Black consistent edge pieces: ", myVal , " White consistent edge pieces: ", oppVal)
    return 0

board = [[-1, 0, 0, 0, 0, 0, -1, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[-1, 0, 0, 0, 0, 0, 0, -1],
[1, 1, 1, 1, 1, 1, 0, -1]]

stability(board, -1)
