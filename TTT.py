import numpy as np

board1 = [' ']*10



#functies
def boardmaker(board):
    #making a board/layout of the values in variable board1 from index 1-9
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])


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

player1, player2 = playerchoose()


def detector():
    #should detect if there is a winner or not
    pass

def takingturns(board):
    #makes sure every player takes its turn 
    for i in range(9):
        if i%2 == 0:
            print('Player 1, do your move. ')
            picksystem(board,player1)
        
        else:
            print('Player 2, move. ')
            picksystem(board,player2)
        

def picksystem(board, player):
    
    cell = ' '
    #choosing the cell
    
    row = input('Which row do you want to mutate? ')
    column = input('Which column do you want to mutate? ')
    
    
    if row == 1:
        cell = board[column]
    
    elif row == 2:
        cell = board[column+3]

    elif row == 3:
        cell = board[column+6]

    return cell




    
'''
    while cell != ' ':
        print('That cell is already in use. Try again. ')
        row = input('Which row do you want to mutate? ')
        column = input('Which column do you want to mutate? ')
        if row == 1:
            cell = board[column]

        elif row == 2:
            cell = board[column+3]

        elif row == 3:
            cell = board[column+6]
'''