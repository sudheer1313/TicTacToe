#intialize the game board
#game board
#user input
#checking the result
#
import random
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
current_player="x"
winner=None
game_running=True
def display_game(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("------------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("------------")
    print(board[6]+" | "+board[7]+" | "+board[8])
def player_input(board):
    inp=int(input("enter a number between 1 and 9:   "))
    if board[inp-1]=="-":
        board[inp-1]=current_player
    else:
        print("The position is already filled")
        display_game(board)
        player_input(board)
def horizontal_check(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True
def row_check(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
def diagnal_check(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True
def check_winner(board):
    global game_running
    if horizontal_check(board):
        display_game(board)
        print("The winner is {}".format(winner))
        game_running=False
    elif row_check(board):
        display_game(board)
        print("The winner is {}".format(winner))
        game_running = False
    elif diagnal_check(board):
        display_game(board)
        print("The winner is {}".format(winner))
        game_running = False
def check_tie(board):

    global game_running
    if "-" not  in board:
        display_game(board)
        print("Its a tie")
        game_running=False
def switch_player():

    global current_player
    if current_player=="x":
        current_player="o"
    else:
        current_player="x"
def computer_turn(board):
    global current_player
    while current_player=="o":
        pos=random.randint(0,8)
        if board[pos]=="-":
            board[pos]="o"
            switch_player()
while game_running:
    display_game(board)
    player_input(board)
    check_winner(board)
    #check_tie(board)
    switch_player()
    computer_turn(board)
    check_winner(board)
    #check_tie(board)











