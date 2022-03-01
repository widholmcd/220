"""
Name: Calvin Widholm
hw7.py

Problem: Creating a simulation of how bumper cars ineteract

Certification of Authenticity:
I certify that this assignment is entirely my own work.- CW
"""

from random import randint
from graphics import GraphWin, Point, Circle, color_rgb
from math import sqrt
import time

def get_random(move_amt):
    random_var = randint(- abs(move_amt), abs(move_amt))
    return random_var

def did_collide(ball, ball_2):
    center_ball_1 = ball.getCenter()
    radius_ball_1 = ball.getRadius()
    center_ball_2 = ball_2.getCenter()
    radius_ball_2 = ball_2.getRadius()
    x_ball_1 = center_ball_1.getX()
    y_ball_1 = center_ball_1.getY()
    x_ball_2 = center_ball_2.getX()
    y_ball_2 = center_ball_2.getY()
    distance = sqrt(((x_ball_2 - x_ball_1) ** 2) + (y_ball_2 - y_ball_1) ** 2)
    radius_summed = radius_ball_1 + radius_ball_2
    if distance <= radius_summed:
        return True
    else:
        return False

def hit_vertical(ball, win):
    ball_center = ball.getCenter()
    ball_radius = ball.getRadius()
    win_height = win.getHeight()
    ball_y = ball_center.getY()
    distance = abs(ball_y - win_height)
    if distance <= ball_radius:
        return True
    if ball_y <= ball_radius:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    ball_center = ball.getCenter()
    ball_radius = ball.getRadius()
    win_width = win.getWidth()
    ball_x = ball_center.getX()
    distance = abs(ball_x - win_width)
    if distance <= ball_radius:
        return True
    if ball_x <= ball_radius:
        return True
    else:
        return False

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color_car = color_rgb(red, green, blue)
    return color_car

def bumper():
    win = GraphWin("bumper", 700, 700)
    ball_x = randint(31, 669)
    ball_y = randint(31, 669)
    ball_radius = 30
    ball = Circle(Point(ball_x, ball_y), ball_radius)
    ball.setFill(get_random_color())
    ball.draw(win)
    ball_2_x = randint(31, 669)
    ball_2_y = randint(31, 669)
    ball_2 = Circle(Point(ball_2_x, ball_2_y), ball_radius)
    ball_2.setFill(get_random_color())
    ball_2.draw(win)


    dx_1 = get_random(15)
    dy_1 = get_random(15)
    dx_2 = get_random(15)
    dy_2 = get_random(15)

    while not win.checkMouse():
        ball.move(dx_1, dy_1)
        ball_2.move(dx_2, dy_2)
        if did_collide(ball, ball_2):
            dx_1 = -dx_1
            dy_1 = -dy_1
            dx_2 = -dx_2
            dy_2 = -dy_2
        if hit_vertical(ball, win):
            dy_1 = -dy_1
        if hit_vertical(ball_2, win):
            dy_2 = -dy_2
        if hit_horizontal(ball, win):
            dx_1 = -dx_1
        if hit_horizontal(ball_2, win):
            dx_2 = -dx_2
        time.sleep(.1)

    win.close()

