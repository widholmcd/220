"""
Name: Calvin Widholm
algorithms.py

Problem: returning a list from a file of numbers and checking if a value is in a list via linear search

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

def read_data(filename):
    evaluated_list = []
    opened = open(filename, 'r')
    words = opened.read()
    modified_words = words.rstrip()
    one_line = modified_words.replace('\n', ' ')
    number_split = one_line.split(' ')
    i = 0
    while i < len(number_split):
        term = number_split[i]
        evaluated_term = eval(term)
        evaluated_list.append(evaluated_term)
        i += 1
    opened.close()
    return evaluated_list

def is_in_linear(search_val, values:list):
    i = 0
    while i < len(values):
        term = values[i]
        if search_val == term:
            return True
        i += 1
    return False

