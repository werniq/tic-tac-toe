from _inc.board import *
from _inc.choice import *
from _inc.input import *


def win_check(human: str, cpu: str) -> bool:
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('[HUMAN] wins the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                print('[Computer] wins the match!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        if not new_game():
            return False
    return True



def new_game() -> bool:
    display_board()
    while True:
        nxt = input('[HUMAN] Do you want to play again?(y/n):')
        if nxt in['y','Y']:
            again = True
            break
        elif nxt in ['n','N']:
            print('Have a great day')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        print('__________NEW GAME__________')
        main_game()
    else:
        return False


def main_game():
    global board
    play = True
    human , computer = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human , computer)
            if play:
                o = computer_input(computer , human , board)
                print(f'[Computer] Entered:{o}')
                board[o] = computer
                display_board()
                play = win_check(human , computer)
        else:
            x = computer_input(computer , human , board)
            print(f'[Computer] Entered:{x}')
            board[x] = computer
            display_board()
            play = win_check(human , computer)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human , computer)


if __name__ == '__main__':
    main_game()
