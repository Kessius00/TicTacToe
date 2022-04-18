#board1 = [' ']*10
board2 = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


#functies
def boardlayout(board):
    #making a board/layout of the values in variable board1 from index 1-9
    print(board[1],'|',board[2],'|',board[3])
    print('- | - | -')
    print(board[4],'|',board[5],'|',board[6])
    print('- | - | -')
    print(board[7],'|',board[8],'|',board[9])


def playerchoose():
    #decides player 1 and player 2
    player1 = ''
    
    while player1 != 'X' and player1 != 'O':
        player1 = input('Which do you want to be? X or O? ').upper()
    
    #define player 2 based on player 1
    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 = 'X'
    return (player1, player2)

#player1, player2 = playerchoose()


def pickcell(board):
    #asks and returns the cell the player wants to mutate

    #choosing the row with a while loop
    row = input('Which row do you want to mutate? ')

    while row.isnumeric() == False and row not in range(1,4):
        row = input('Which row do you want to mutate? ')
    
    #choosing the column with a while loop
    column = input('Which column do you want to mutate? ')

    while column.isnumeric() == False and column not in range(1,4):
        column = input('Which column do you want to mutate? ')

    row = int(row)
    column = int(column)

    #converting the rows and columns into cells in the board
    if row == 1:
        cell = board[column]
    
    elif row == 2:
        cell = board[column+3]

    elif row == 3:
        cell = board[column+6]
    
    celindex = (board.index(cell))

    return celindex, cell


def boxchecker(board):
    #checks if the cell picked is empty and can be mutated, if not, pickcell
    celindex, cell = pickcell(board)

    while cell != int:
        celindex, cell = pickcell(board)
    
    return celindex, cell


def mutator(board, player):
    #mutates the board for the given cell

    celindex = boxchecker(board)

    board[celindex] = player
    
    return board


def playing(board):

    player1, player2 = playerchoose()

    boardlayout(board)

    for i in range(9):
        if i%2 == 0:
            print('Player 1, do your move. ')
            mutator(board, player1)
            boardlayout(board2)
        
        else:
            print('Player 2, move. ')
            mutator(board, player2)
            boardlayout(board2)
    
    

playing(board2)




def detector():
    #should detect if there is a winner or not
    pass

 