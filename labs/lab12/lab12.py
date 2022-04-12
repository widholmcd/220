"""
Name: Calvin Widholm
hw12.py

Problem: Using loops for linear searches and using while loops for various tasks, also creating a number
guessing game

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from random import randint
def find_and_remove_first(input_list:list, value):
    i = 0
    while i < len(input_list):
        term = input_list[i]
        if term == value:
            input_list.remove(term)
            input_list.insert(i, "Calvin")
            i = len(input_list)
        i += 1
    #print(input_list)

def good_input():
    user_input = eval(input('input a number between 1 and 10'))
    while not (1 <= user_input <= 10):
        if user_input > 10:
            print('too high')
        elif user_input < 1:
            print('too low')
        user_input = eval(input('input a number between 1 and 10'))
    return user_input

def num_digits():
    print('to stop enter a 0 or a negative number')
    user_input = eval(input('enter a positive integer'))
    while user_input > 0:
        count = 0
        while user_input > 0:
            user_input = user_input // 10
            count += 1
        if count == 1:
            print(count, 'digit in your number')
        else:
            print(count, 'digits in your number')
        user_input = eval(input('enter a positive integer'))

def hi_lo_game():
    game_determinant = []
    random_number = randint(1, 100)
    guesses = 0
    while not guesses == 7:
        guesses += 1
        print('guess:', guesses)
        user_guess = eval(input('guess a number'))
        if user_guess < random_number:
            print('the guess is too low')
        elif user_guess > random_number:
            print('the guess is too high')
        elif user_guess == random_number:
            print('You win in', guesses, 'guesses!')
            game_determinant.append('w')
            guesses = 7
    if not ('w' in game_determinant):
        print('Sorry, you lose. The number was', random_number)
