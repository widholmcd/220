"""
Name: Calvin Widholm
hw4.py

Problem: Using the math and graphics library to create various objects and do aprroximations

Certification of Authenticity:
I certify that this assignment is entirely my own work.- Calvin Widholm- I certify
"""

import math
from graphics import Rectangle, GraphWin, Point, Text, Circle


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add more squares")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of square

        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        #shape.move(change_x, change_y)
        shape1 = shape.clone()
        shape1.move(change_x, change_y)
        shape1.draw(win)

    closing_remark = Text(Point(200,200), "Click again to close")
    closing_remark.draw(win)


    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    point_a = win.getMouse()
    point_b = win.getMouse()

    shape = Rectangle(point_a, point_b)
    shape.draw(win)
    shape.setFill("green")

    x_point_a = point_a.getX()
    x_point_b = point_b.getX()
    y_point_a = point_a.getY()
    y_point_b = point_b.getY()

    x_length = abs(x_point_b - x_point_a)
    y_height = abs(y_point_b - y_point_a)
    perimeter = (2 * x_length) + (2 * y_height)
    area = x_length * y_height

    perimeter_text = Text(Point(200, 320), "Perimeter:")
    perimeter_text2 = Text(Point(200, 340), perimeter)
    perimeter_text.draw(win)
    perimeter_text2.draw(win)

    area_text = Text(Point(200, 360), "Area:")
    area_text2 = Text(Point(200, 380), area)
    area_text.draw(win)
    area_text2.draw(win)

    closing_remark = Text(Point(200, 200), "Click again to close")
    closing_remark.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    center = win.getMouse()
    circumf_point = win.getMouse()

    x_value_1 = center.getX()
    x_value_2 = circumf_point.getX()
    y_value_1 = center.getY()
    y_value_2 = circumf_point.getY()

    radius = math.sqrt(((x_value_2 - x_value_1) ** 2) + ((y_value_2 - y_value_1) ** 2))

    shape = Circle(center, radius)
    shape.draw(win)
    shape.setFill("teal")

    radius_text = Text(Point(200, 350), "Radius:")
    radius_text2 = Text(Point(200, 370), radius)
    radius_text.draw(win)
    radius_text2.draw(win)

    closing_remark = Text(Point(200,200), "Click again to close")
    closing_remark.draw(win)

    win.getMouse()
    win.close()



def pi2():
    terms = eval(input("Enter the number of terms to sum:"))
    approx = 0
    for i in range(0, 2 * terms, 2):
        approx = (4 / (i + 1)) * ((-1) ** (i // 2)) + approx
    print("pi approximation:", approx)
    accuracy = abs(math.pi - approx)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    pass
