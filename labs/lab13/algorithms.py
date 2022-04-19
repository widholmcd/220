"""
Name: Calvin Widholm
algorithms.py

Problem: this week sorting lists of values using a selection sort and sorting areas of rectangles via this

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from graphics import Point, Rectangle

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


def selection_sort(values):
    min_value_list = []
    counting_list = []
    for i in range(len(values)):
        min_value = values[i]
        count = 0 + i
        while count < len(values):
            if min_value > values[count]:
                min_value = values[count]
                counting_list.append(count)
            if min_value == values[count]:
                counting_list.append(count)
            count += 1
        if min_value not in min_value_list:
            min_value_list.append(min_value)
            index = values.index(min_value)
        else:
            index = counting_list[-1]
        values[i], values[index] = values[index], values[i]


def calc_area(rect:Rectangle):
    point_1 = rect.getP1()
    point_2 = rect.getP2()
    point_1_x = point_1.getX()
    point_2_x = point_2.getX()
    point_1_y = point_1.getY()
    point_2_y = point_2.getY()

    length = abs(point_2_x - point_1_x)
    height = abs(point_2_y - point_1_y)
    area = length * height
    return area


def rect_sort(rectangles):
    min_value_list = []
    counting_list = []
    for i in range(len(rectangles)):
        min_value = rectangles[i]
        count = 0 + i
        while count < len(rectangles):
            if calc_area(min_value) > calc_area(rectangles[count]):
                min_value = rectangles[count]
                counting_list.append(count)
            if calc_area(min_value) == calc_area(rectangles[count]):
                counting_list.append(count)
            count += 1
        if min_value not in min_value_list:
            min_value_list.append(min_value)
            index = rectangles.index(min_value)
        else:
            index = counting_list[-1]
        rectangles[i], rectangles[index] = rectangles[index], rectangles[i]
