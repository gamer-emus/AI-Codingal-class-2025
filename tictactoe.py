import random
#from colorama import init, Fore, Style
#init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return  cell 
        elif cell == 'O':
            return  cell 
        else:
            return  cell 
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print( '-----------' )
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print( '-----------' )
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input( "Do you want to be X or O? " ).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



def player_move(Board,symbol):
    move = -1
    while move not in range(1,10) or not Board[move -1 ].isdigit():
        try:
            move = int(input("Enter Your move (1-9)"))
            if move not in range(1,10) or not Board[move -1].isdigit():
                print("Invalid move , Please try again")
        except ValueError:
            print("Please enter a number between 1-9")
    Board[move - 1] = symbol

def ai_move(Board, ai_symbol, player_symbol):
    for i in range(9):
        if Board[i].isdigit():
            Board_copy = Board.copy()
            Board_copy[i]= ai_symbol
            if check_win(Board_copy, ai_symbol):
                Board[i] = ai_symbol
                return
    for i in range(9):
        if Board[i].isdigit():
            Board_copy = Board_copy()
            Board_copy[1] = player_symbol
            if check_win(Board_copy , player_symbol):
                Board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if Board[i].isdigit()]
    move = random.choice(possible_moves)
    Board[move] = ai_symbol


def check_win(board, symbol):

    win_conditions = [

        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal

        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical

        (0, 4, 8), (2, 4, 6)
    
    ]

    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return  True
    return False

def check_full(Board):
    return all(not spot.isdigit() for spot in Board)



            







def ttt():
    print("Welcome! to Tic-Tac-Toe")
    player_name = input( "Enter Your name " )
    while True:
        Board = ['1','2','3','4','5','6','7','8','9']
        player_sybol, ai_symbol = player_choice()
        turn = "Player"
        game_on = True


        while game_on:
            display_board(Board)
            if turn == "Player":
                player_move(Board, player_sybol)
            if check_win(Board, player_sybol):
                display_board(Board)
                print("Congratulations "+ player_name + ", You have won the game!")
                game_on = False
            else:
                if check_full(Board):
                    display_board(Board)
                    print("Its a Tie!")
                    break
                else:
                    turn = "AI"
        else:
            ai_move(Board,ai_symbol, player_sybol)
            if check_win(Board, ai_symbol):
                display_board(Board)
                print("Ai Has Won the Game!")
                game_on = False
            else:
                if check_full(Board):
                    display_board(Board)
                    print("Its a Tie!")
                    break
                else:
                    turn = 'Player'

        play_again = input("Do you want to play again (yes/no)").lower()
        if play_again != 'yes':
            print("Thank you for playing")
            break



if __name__ == "__main__":
    ttt()
                

        


