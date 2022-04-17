# Sudoku is a game played on a 9x9 grid. 
# The goal of the game is to fill all cells of the grid with digits from 1 to 9, 
# so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
# (More info at: http://en.wikipedia.org/wiki/Sudoku)
# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing 
# a Sudoku board, and returns true if it is a valid solution, or false otherwise. 
# The cells of the sudoku board may also contain 0's, which will represent empty cells. 
# Boards containing one or more zeroes are considered to be invalid solutions.
# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.


def valid_solution(board):
    res = True
    for i in board:
        if 0 in i or len(set(i)) != len(i):
            res = False
    rows = []
    a = 0
    while a != 8:
        rows.append([board[i][a] for i in range(len(board))])
        a += 1
    for i in rows:
        if 0 in i or len(set(i)) != len(i):
            res = False
    fes = []
    for i in board:
        for x in i:
            fes.append(x)

    square1 = []
    for i in range(0, len(fes), 9):
        square1.append(fes[i:i+3])
    square2 = []
    for i in range(3, len(fes), 9):
        square2.append(fes[i:i+3])
    square3 = []
    for i in range(6, len(fes), 9):
        square3.append(fes[i:i+3])

    for x in range(0, len(square1), 3):
        square1[x] = square1[x:x+3]
    del square1[1:3], square1[5:7], square1[3], square1[2]

    for x in range(0, len(square2), 3):
        square2[x] = square2[x:x+3]
    del square2[1:3], square2[5:7], square2[3], square2[2]

    for x in range(0, len(square3), 3):
        square3[x] = square3[x:x+3]
    del square3[1:3], square3[5:7], square3[3], square3[2]
    r = []
    for x in square1, square2, square3:
        for i in x:
            for y in i:
                for k in y:
                    r.append(k)
    f = []
    for i in range(0, len(r), 9):
        f.append(r[i:i+9])

    for i in f:
        if 0 in i or len(set(i)) != len(i):
            res = False
    return res
  
  
  
  print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
