"""
Name: Calvin Widholm
face.py

Problem: Creating methods to make a face smile, display shock, or wink

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from graphics import Circle, Line, Point


class Face:
    """
    Face constructor
    """
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        point_3 = self.mouth.getCenter()
        point_1 = self.mouth.getP1()
        point_2 = self.mouth.getP2()
        point_1_x = point_1.getX()
        point_3_x = point_3.getX()
        point_3.move(0, abs(point_3_x - point_1_x))
        mouth_line_a = Line(point_1, point_3)
        mouth_line_b = Line(point_2, point_3)
        mouth_line_a.draw(self.window)
        mouth_line_b.draw(self.window)


    def shock(self):
        self.mouth.undraw()
        radius = self.left_eye.getRadius()
        mouth_height = self.mouth.getCenter()
        mouth_height_y = mouth_height.getY()
        left_center = self.left_eye.getCenter()
        right_center = self.right_eye.getCenter()
        left_x = left_center.getX()
        right_x = right_center.getX()
        middle = (right_x + left_x) / 2
        shock_mouth = Circle(Point(middle, mouth_height_y), radius)
        shock_mouth.draw(self.window)


    def wink(self):
        Face.smile(self)
        left_radius = self.left_eye.getRadius()
        self.left_eye.undraw()
        point_1_x_start = self.mouth.getP1()
        point_1_x = point_1_x_start.getX()
        point_1_y_start = self.left_eye.getCenter()
        point_1_y = point_1_y_start.getY()
        point_2_x = point_1_x + (2 * left_radius)
        left_eye = Line(Point(point_1_x, point_1_y), Point(point_2_x, point_1_y))
        left_eye.draw(self.window)



