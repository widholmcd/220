"""
Name: Calvin Widholm
lab5.py

Problem: Using the graphics library to make objects as well as indexing lists and strings

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""

from math import sqrt
from graphics import GraphWin, Point, Polygon, Text, Entry, Circle, color_rgb


def triange():
    win = GraphWin("Triangle", 400, 400)
    instructions = Text(Point(200, 25), "Click 3 different places to draw a triangle")
    instructions.draw(win)

    point_a = win.getMouse()
    point_b = win.getMouse()
    point_c = win.getMouse()

    triangle = Polygon(point_a, point_b, point_c)
    triangle.setFill("yellow")
    triangle.draw(win)

    point_a_x = point_a.getX()
    point_a_y = point_a.getY()
    point_b_x = point_b.getX()
    point_b_y = point_b.getY()
    point_c_x = point_c.getX()
    point_c_y = point_c.getY()

    dx_a = point_a_x - point_b_x
    dx_b = point_b_x - point_c_x
    dx_c = point_a_x - point_c_x
    dy_a = point_a_y - point_b_y
    dy_b = point_b_y - point_c_y
    dy_c = point_a_y - point_c_y

    length_a = sqrt((dx_a ** 2) + (dy_a ** 2))
    length_b = sqrt((dx_b ** 2) + (dy_b ** 2))
    length_c = sqrt((dx_c ** 2) + (dy_c ** 2))

    perimeter = length_a + length_b + length_c
    s_value = (length_a + length_b + length_c) / 2
    area = sqrt(s_value * (s_value - length_a) * (s_value - length_b) * (s_value - length_c))

    perimeter_text_a = Text(Point(200,300), "Perimeter:")
    perimeter_text_b = Text(Point(200, 320), perimeter)
    area_text_a = Text(Point(200, 340), "Area:")
    area_text_b = Text(Point(200, 360), area)
    perimeter_text_a.draw(win)
    perimeter_text_b.draw(win)
    area_text_a.draw(win)
    area_text_b.draw(win)

    closing_remark = Text(Point(200, 380), "Click to Close")
    closing_remark.draw(win)
    win.getMouse()
    win.close()



def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_entry.draw(win)


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_entry.draw(win)


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_entry.draw(win)


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)




    for i in range(5):
        instruction_text = Text(Point(200, 20), "Click to Start Color Conversion!")
        instruction_text.setTextColor("black")
        instruction_text.draw(win)
        win.getMouse()
        red_string = red_entry.getText()
        red_color = eval(red_string)
        green_string = green_entry.getText()
        green_color = eval(green_string)
        blue_string = blue_entry.getText()
        blue_color = eval(blue_string)
        insert_color = color_rgb(red_color, green_color, blue_color)
        shape.setFill(insert_color)
        instruction_text.setTextColor("white")

    # Wait for another click to exit
    closing_instructions = Text(Point(200, 40), "Click Once To Close")
    closing_instructions.draw(win)
    win.getMouse()
    win.close()


def process_string():
    string_text = input("Enter any word, sentence, anything really!")
    string_length = len(string_text)
    first_character = string_text[0]
    print("First Character:", first_character)
    last_character = string_text[string_length - 1]
    print("Last Character:", last_character)
    characters_in_pos = string_text[1:5]
    in_pos_string = "".join(characters_in_pos)
    print("Characters from Positions 2-5:", in_pos_string)
    concatination = first_character + last_character
    print("Concatenation of the first and last character:", concatination)
    first_three = string_text[0:3]
    first_three_string = "".join(first_three)
    for _ in range(10):
        print(first_three_string, end=" ")
    print()
    for i in range(0, string_length):
        string_parse = string_text[i]
        print(string_parse)
    print("Number of Characters:", string_length)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x_value = values[1:4:2]
    x_value = "".join(x_value)
    print("1:", x_value)
    x_value = str(str(values[0]) +str(" ") + str("+") + str(" ") + str(values[2]))
    print("2:", x_value)
    x_value = values[1] + values[1] + values[1] + values[1] + values[1]
    print("3:", x_value)
    x_value = values[2:5]
    print("4:", x_value)
    x_value = values[2:4] + values[0:1]
    print("5:", x_value)
    x_value = float(values[5])
    x_value = values[2:3] + values[0:1] + [x_value]
    print("6:", x_value)
    x_value = float(values[5])
    x_value = (str(x_value))
    x_value = str(str(values[0]) + " + " + str(values[2]) + " + " + (x_value))
    print("7:", x_value)
    x_value = len(values)
    print("number of items in list:", x_value)

    # not sure if summations were to be the actual sum of the printed addition problem
    # below are the actual sums of 2 and 7

    print()
    print("Below are the summations of problem 2 and 7")
    x_value = values[0] + values[2]
    print("2:", x_value)
    x_value = float(values[5])
    x_value = values[0] + values[2] + x_value
    print("7:", x_value)




def another_series():
    terms = eval(input("Enter the number of terms you would like to sum:"))
    start = 0
    for i in range(terms):
        series = 2 * (i % 3) + 2
        start = start + series
    print("sum =", start)



def target():
    win = GraphWin("Target", 500, 500)
    center_point = Point(250, 250)

    circle_a = Circle(center_point, 250)
    circle_a.setFill("white")
    circle_a.draw(win)

    circle_b = Circle(center_point, 200)
    circle_b.setFill("black")
    circle_b.draw(win)

    circle_c = Circle(center_point, 150)
    circle_c.setFill("blue")
    circle_c.draw(win)

    circle_d = Circle(center_point, 100)
    circle_d.setFill("red")
    circle_d.draw(win)

    circle_e = Circle(center_point, 50)
    circle_e.setFill("yellow")
    circle_e.draw(win)


    closing_statement = Text(Point(250, 480), "Click Once to Close")
    closing_statement.draw(win)
    win.getMouse()
    win.close()
