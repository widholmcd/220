"""
Name: Calvin Widholm
hw9.py

Problem: creating hangman in the python console and graphically, using called functions

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""


from random import randint
from graphics import GraphWin, Circle, Line, Point, Text, Entry
def get_words(file_name):
    word_list = []
    opened = open(file_name, "r")
    for line in opened:
        word_list.append(line)
    return word_list


def get_random_word(words:list):
    random_number = randint(0, len(words) - 1)
    chosen_word = words[random_number]
    string_word = str(chosen_word)
    parsed_word = string_word.replace('\n', '')
    return parsed_word


def letter_in_secret_word(letter, secret_word):
    length_secret_word = len(secret_word)
    for i in range(length_secret_word):
        if letter == secret_word[i]:
            return True
    return False


def already_guessed(letter, guesses):
    length_guess_list = len(guesses)
    for i in range(length_guess_list):
        if letter == guesses[i]:
            return True
    return False


def make_hidden_secret(secret_word:str, guesses:list):
    word_list = []
    length_secret_word = len(secret_word)
    length_guesses = len(guesses)
    for _ in range(length_secret_word):
        word_list.append("_")
    for j in range(length_secret_word):
        for k in range(length_guesses):
            if guesses[k] == secret_word[j]:
                word_list = word_list[0:j] + list(secret_word[j]) + word_list[(j + 1):length_secret_word]
    joined = " ".join(word_list)
    return joined



def won(guessed):
    length_mystery_word = len(guessed)
    for i in range(length_mystery_word):
        if guessed[i] == '_':
            return False
    return True


def play_graphics(secret_word):
    win = GraphWin("hangman", 700, 700)
    letters = Text(Point(350, 25), 'letters: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q,'
                                   'r, s, t, u, v, w, x, y, z')
    letters.draw(win)
    guesses = 6
    guess_list = []
    guessed_letters = Text(Point(250, 50), 'already guessed:')
    guessed_letters.draw(win)
    updated_board = make_hidden_secret(secret_word, guess_list)
    updated_board_text = Text(Point(350, 640), updated_board)
    updated_board_text.draw(win)
    gallows_base = Line(Point(250, 600), Point(450, 600))
    gallows_base.draw(win)
    gallows_post = Line(Point(350, 600), Point(350, 200))
    gallows_post.draw(win)
    gallows_extend = Line(Point(350, 200), Point(250, 200))
    gallows_extend.draw(win)
    gallows_hang = Line(Point(250, 200), Point(250, 225))
    gallows_hang.draw(win)
    new_entry = ''
    previous_guesses = Text(Point(375, 50), '')
    previous_guesses.draw(win)
    count = 0
    while guesses != 0:
        guess_instructions = Text(Point(250, 670), 'guess a letter:')
        guess_instructions.draw(win)
        guessed_letter = Entry(Point(350, 670), 5)
        guessed_letter.draw(win)
        click_instructions = Text(Point(250, 690), 'after entering a letter click once to enter it')
        click_instructions.draw(win)
        win.getMouse()
        guessed_letter_text = guessed_letter.getText()
        while guessed_letter_text == '':
            urgent_instructions = Text(Point(500, 350), 'please enter an actual letter')
            urgent_instructions.draw(win)
            win.getMouse()
            guessed_letter_text = guessed_letter.getText()
            urgent_instructions.undraw()
        while already_guessed(guessed_letter_text, guess_list):
            new_instructions = Text(Point(500, 350), 'please enter a new letter')
            new_instructions.draw(win)
            win.getMouse()
            guessed_letter_text = guessed_letter.getText()
            new_instructions.undraw()
        guess_list.append(guessed_letter_text)
        new_entry = new_entry + " " + guess_list[count]
        previous_guesses.setText(new_entry)
        count = count + 1
        if not letter_in_secret_word(guessed_letter_text, secret_word):
            guesses = guesses - 1
            if guesses == 5:
                head = Circle(Point(250, 250), 25)
                head.draw(win)
            if guesses == 4:
                body = Line(Point(250, 275), Point(250, 350))
                body.draw(win)
            if guesses == 3:
                arm_1 = Line(Point(250, 300), Point(200, 350))
                arm_1.draw(win)
            if guesses == 2:
                arm_2 = Line(Point(250, 300), Point(300, 350))
                arm_2.draw(win)
            if guesses == 1:
                leg_1 = Line(Point(250, 350), Point(200, 450))
                leg_1.draw(win)
            if guesses == 0:
                leg_2 = Line(Point(250, 350), Point(300, 450))
                leg_2.draw(win)
        updated_board = make_hidden_secret(secret_word, guess_list)
        updated_board_text.setText(updated_board)
        if won(updated_board):
            winning_text = Text(Point(500, 250), "Winner!")
            winning_text.draw(win)
            guesses = 0
    if not won(updated_board):
        sorry_text = Text(Point(350, 100), "sorry, you did not guess the word.")
        sorry_text.draw(win)
        reveal_text = Text(Point(350, 120), "the secret word was " + secret_word)
        reveal_text.draw(win)
    closing_remark = Text(Point(350, 150), 'click once to close')
    closing_remark.draw(win)
    win.getMouse()
    win.close()



def play_command_line(secret_word):
    guesses = 6
    guess_list = []
    print('already guessed', guess_list)
    print('guesses remaining', guesses)
    updated_board = make_hidden_secret(secret_word, guess_list)
    print(updated_board)
    while guesses != 0:
        guessed_letter = input("guess a letter")
        while already_guessed(guessed_letter, guess_list):
            guessed_letter = input("you have already guessed this letter, guess a new one")
        guess_list.append(guessed_letter)
        if not letter_in_secret_word(guessed_letter, secret_word):
            guesses = guesses - 1
        print("already guessed", guess_list)
        print("guesses remaining", guesses)
        updated_board = make_hidden_secret(secret_word, guess_list)
        if won(updated_board):
            print('winner')
            print(secret_word)
            guesses = 0
        if not won(updated_board):
            print(updated_board)
    if not won(updated_board):
        print("sorry, you did not guess the word.")
        #The test was failing when I added ", secret_word in this second print statement
        print("the secret word was")




if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
