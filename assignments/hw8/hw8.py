"""
Name: Calvin Widholm
hw8.py

Problem: using accumulations and modifying parameters, also using conditionals for tasks

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""

from math import sqrt
from graphics import Circle, GraphWin, Text, Point


def add_ten(nums: list[int]):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums: list):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums: list):
    len_list = len(nums)
    additive = 0
    for i in range(len_list):
        additive = additive + nums[i]
    return additive


def to_numbers(nums: list[str]):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums: list[str]):
    split_string_list = []
    output_list = []
    for i in range(len(nums)):
        split_string = nums[i].split(",")
        split_string_list.append(split_string)
    for j in split_string_list:
        to_numbers(j)
        print(j)
        square_each(j)
        total = sum_list(j)
        output_list.append(total)
    return output_list



def starter(weight, wins: int):
    if ((150 <= weight < 160) and (wins >= 5)) or ((weight > 199) or (wins > 20)):
        return True
    return False


def leap_year(year: int):
    if (year % 400) == 0:
        return True
    if (year % 100) == 0:
        return False
    if (year % 4) == 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 +
        (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_two = Circle(center_2, radius_2)
    circle_two.setFill("green")
    circle_two.draw(win)

    overlap_check = did_overlap(circle_one, circle_two)
    if overlap_check == False:
        message = Text(Point(5, 9), "The circles do not overlap")
        message.draw(win)
    if overlap_check == True:
        message_2 = Text(Point(5, 1), "The circles overlap")
        message_2.draw(win)
    closing_remark = Text(Point(5, .5), "Click again to close")
    closing_remark.draw(win)
    win.getMouse()
    win.close()



def did_overlap(circle_one: Circle, circle_two: Circle):
    circle_one_center = circle_one.getCenter()
    circle_two_center = circle_two.getCenter()
    circle_one_x = circle_one_center.getX()
    circle_one_y = circle_one_center.getY()
    circle_two_x = circle_two_center.getX()
    circle_two_y = circle_two_center.getY()
    distance = sqrt(((circle_two_x - circle_one_x) ** 2) + ((circle_two_y - circle_one_y) ** 2))
    circle_one_radius = circle_one.getRadius()
    circle_two_radius = circle_two.getRadius()

    if distance > (circle_one_radius + circle_two_radius):
        return False
    return True


if __name__ == '__main__':
    pass
