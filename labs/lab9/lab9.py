"""
Name: Calvin Widholm
lab9.py

Problem: Creating the tic tac toe game inside of python and playing it

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    indexed_value = position - 1
    spot_in_question = board[indexed_value]
    string_spot_in_question = str(spot_in_question)
    choice = string_spot_in_question.isnumeric()
    if choice == True:
        return True
    else:
        return False


def fill_spot(board:list, position, character:str):
    lower_character = character.lower()
    indexed_value = position - 1
    board[indexed_value] = lower_character
    specific_value = board[indexed_value]
    list_specific_value = list(specific_value)
    pre_list = board[0:indexed_value]
    post_list = board[position:9]
    board = pre_list + list_specific_value + post_list


def winning_game(board):
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6]:
            return True
        if board[3 * i] == board[(3 * i) + 1] == board[(3 * i) + 2]:
            return True

    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    else:
        return False


def game_over(board):
    #Testing if each position is numeric
    cat_game_list = []
    for i in range(9):
        pos_i = board[i]
        str_pos_i = str(pos_i)
        choice = str_pos_i.isnumeric()
        if choice == True:
            cat_element = False
            cat_game_list.append(cat_element)
        else:
            cat_element = True
            cat_game_list.append(cat_element)
    if cat_game_list == [True, True, True, True, True, True, True, True, True]:
        cat_game = True
    else:
        cat_game = False
    if (winning_game(board) or cat_game) == True:
        return True
    else:
        return False


def get_winner(board):
    if game_over(board) == True:
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6]:
                return board[i]
            if board[3 * i] == board[(3 * i) + 1] == board[(3 * i) + 2]:
                return board[3 * i]

        if board[0] == board[4] == board[8]:
            return board[0]
        if board[2] == board[4] == board[6]:
            return board[2]
        else:
            return "Nobody! Cat's Game!"
    if game_over(board) == False:
        return None


def play(board:list):
    print("Welcome to tic tac toe! Here you see a board numbered 1-9.",
          "To start x's will choose which number",
          "they want to go with. Then o will follow")
    play_question = input("Do you want to play?")
    indexed_question = play_question[0]
    while indexed_question == 'y':
        turn_count = 0
        game_board = build_board()
        print_board(game_board)
        while not game_over(game_board):
            what_turn = turn_count % 2
            turn_count = turn_count + 1
            if what_turn == 0:
                what_turn = 'x'
            if what_turn == 1:
                what_turn = 'o'
            position = eval(input("What position would you like?"))
            while is_legal(game_board, position) == False:
                position = eval(input("Enter a valid position please"))
            fill_spot(game_board, position, what_turn)
            print_board(game_board)
        winner = get_winner(game_board)
        print("The winner is", winner)
        play_question = input("Do you want to play?".lower())
        indexed_question = play_question[0]







def main():
    pass


if __name__ == '__main__':
    main()
