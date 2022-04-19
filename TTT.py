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
    row = input('Which row do you want to mutate? (1-3) ')

    while row.isnumeric() == False or int(row) not in range(1,4):
        row = input('Which row do you want to mutate? (1-3) ')
    
    #choosing the column with a while loop
    column = input('Which column do you want to mutate? (1-3) ')

    while column.isnumeric() == False or int(column) not in range(1,4):
        column = input('Which column do you want to mutate? (1-3) ')

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


def boxchecker(board, players, player):
    #checks if the cell picked is empty and can be mutated, if not, pickcell
    celindex, cell = pickcell(board)
    
    #nog ff fixen dat je niet twee keer op een gemuteerd vakje zit
    while cell not in board:
        celindex, cell = pickcell(board)
    
    board[celindex] = player

    return board

def landoccupied(player, board):
    #gives a percentage of the occupied boxes on the board of the player
    x = board.count(player)
    y = round((x*100)/(len(board)-1),1)
    print(f'You have occupied {y} % of the board')

def detector(board,player):
    #should detect if there is a winner or not

    for i in board[1:]:
        #horizontally
        if i in (1,4,7) and board[i] == board[i+1] and board[i] == board[i+2]:
            print(f'{player} wins')
            return 1
        #vertically 
        elif i in (1,2,3) and board[i] == board[i+3] and board[i] == board[i+6]:
            print(f'{player} wins')
            return 1
        #diagonally decreasing
        elif i == 1 and board[i] == board[i+4] and board[i] == board[i+8]:
            print(f'{player} wins')
            return 1
        #diagonally increasing
        elif i == 3 and board[i] == board[i+2] and board[i] == board[i+4]:
            print(f'{player}')
    return 0


def turn(board, players, player):
    #every action each player undergoes each turn
    landoccupied(player, board)
    nb = boxchecker(board, players, player)
    boardlayout(nb)
    detector(board, player)

def playing(board):
    #the total number of turns is chosen here, the game will be performed in this function
    player1, player2 = playerchoose()
    boardlayout(board)
    
    for i in range(10):
        if i%2 == 0:
            print('Player 1, do your move. ')
            turn(board, (player1, player2), player1)
        
        else:
            print('Player 2, move. ')
            turn(board, (player1, player2), player2)
        

playing(board2)
