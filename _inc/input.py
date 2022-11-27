from _inc.board import *


def computer_input(computer: int, human: int, board: list) -> int:
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,computer):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,human):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i


def human_input(number: int) -> int:
    while True:
        inp = input(f"[HUMAN] '{number}' Enter your choice:")
        if inp.isdigit() and int(inp) <10 and int(inp) >0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[HUMAN] '{number}' place already taken.")
        else:
            print(f"[HUMAN] '{number}' Enter valid option (1 - 9).")


def win_move(i: int, board: list, mark: int) -> bool:
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False


def winning(number: int, board: list[int]) -> bool:
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == number:
            return True

