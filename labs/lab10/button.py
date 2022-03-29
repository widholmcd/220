"""
Name: Calvin Widholm
button.py

Problem: Creating a button class with methods to use in main

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""

from graphics import Rectangle, Point, Text, GraphWin
class Button:
    def __init__(self, shape:Rectangle, label:str):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label:str):
        self.text.setText(label)

    def draw(self, win:GraphWin):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point:Point):
        x_var = point.getX()
        y_var = point.getY()
        button_point_1 = self.shape.getP1()
        button_point_2 = self.shape.getP2()
        button_point_1_x = button_point_1.getX()
        button_point_1_y = button_point_1.getY()
        button_point_2_x = button_point_2.getX()
        button_point_2_y = button_point_2.getY()
        if (button_point_1_x <= x_var <= button_point_2_x) and (button_point_1_y <= y_var <= button_point_2_y):
            return True
        else:
            return False

    def color_button(self, color:str):
        self.shape.setFill(color)



