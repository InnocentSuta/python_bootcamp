# -*- coding: utf-8 -*-
from string import ascii_lowercase
import random
import re
import string



def setBoard(board_size, num_Mines):
  
    emptyBoard = [['0' for i in range(board_size)] for i in range(board_size)]
    
    m = getmines(emptyBoard, num_Mines) #m for mines
    
    for i, x in m:
        emptyBoard[i][x] = '*'
        
    board = getnumbers(emptyBoard)
    
    return (board, m)



def gameBoard(board):
    board_size = len(board)

    horizontal = '   ' + (4 * board_size * '-') 

    toplabel = '   ' #top left corner space

    for i in ascii_lowercase[:board_size]:
        
        toplabel = toplabel + i + '   ' #spacing the letters

    print(toplabel + '\n' + horizontal)


    for x, i in enumerate(board):
        row = f"{x + 1}"
       # row = f'{0:2} '

        for j in i:
            row = row + ' ' + j 

        print(row + '\n' + horizontal)

    print('')
    
    
def getmines(board, mine_size):
    
    m = []
    
    near_Cells = getNearCells(board, mine_size)
    
    for i in range(mine_size):
        
        cell = randomcell(board)
        
        while cell in m or cell in near_Cells:
            cell = randomcell(board)
            m.append(cell)
            
    return m
    
    
def randomcell(board):
    board_size = len(board)
     
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)

    return (x, y)

    

def getNearCells(board, rowNo, colNo):    
    board_size = len(board)
   
    near_Cells = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowNo + i) < board_size and -1 < (colNo + j) < board_size:
                near_Cells.append((rowNo + i, colNo + j))

    return near_Cells
    
    
def getnumbers(board):
    for rowNo, row in board:
        for colNo, cell in row:
            if cell != '*':
                values = [board[r][c] for r, 
                          c in getNearCells(board, rowNo, colNo)]
                board[rowNo][colNo] = str(values.count('*'))

    return board
    
def showcells(board, currboard, r, l):
    if currboard[r][l] != ' ': #check for empty cells if shown exit 
        return
    
    currboard[r][l] = board[r][l] #current board becomes new board
    
    if board[r][l] == '0':
        for row, col in getNearCells(board, r, l):
            if currboard[row][col] != 'Flag':
                #showcells(board, currboard, r, c)
                showcells(board, currboard, row, col)
     
    
    

def mainFunction():
    
    board_size = 8
    num_Mines = 8
    board = []
    
    m = set([])
    
   # flags = {'flags': False}
    
    currboard = [[' * ' for i in range(board_size)] for i in range(board_size)]
    gameBoard(currboard)
    
    userInput = input('Please enter a column and row to reveal(e.g. A8): ')
    
    #checking userinput 
    inputs = r'([a-{}])([0-8]+)(h?)'.format(ascii_lowercase[board_size - 1])
    validateInput = re.match(inputs, userInput)
    
    row = int(validateInput.group(2)) - 1
    col = ascii_lowercase.index(validateInput.group(1))
    
    if -1 < row < board_size:
            cell = (row, col)
#            cell = userInput('cell')

    cell = row, col
    
"""
    while m != mines:
        
        if userInput:
            
           if userInput(row, col) = 'm':
               
               if (row,col) in m:
                   
                    m.remove((row, col))
                    setBoard[(row, col)] = '*'
          """  
        
mainFunction()
    
    