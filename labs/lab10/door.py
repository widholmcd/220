"""
Name: Calvin Widholm
door.py

Problem: Creating a door class with methods to use in main

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""


from graphics import GraphWin, Point, Rectangle, Text
class Door:
    def __init__(self, shape:Rectangle, label:str):
        self.shape = shape
        center = self.shape.getCenter()
        self.text = Text(center, label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label:str):
        return self.text.setText(label)

    def draw(self, win:GraphWin):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point:Point):
        x_var = point.getX()
        y_var = point.getY()
        rec_point_1 = self.shape.getP1()
        rec_point_2 = self.shape.getP2()
        rec_point_1_x = rec_point_1.getX()
        rec_point_1_y = rec_point_1.getY()
        rec_point_2_x = rec_point_2.getX()
        rec_point_2_y = rec_point_2.getY()
        if (rec_point_1_x <= x_var <= rec_point_2_x) and (rec_point_1_y <= y_var <= rec_point_2_y):
            return True
        else:
            return False

    def open(self, color:str, label:str):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color:str, label:str):
        self.shape.setFill(color)
        self.text.setText(label)

    def color(self, color:str):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret == True:
            return True
        else:
            return False

    def set_secret(self, secret:bool):
        self.secret = secret

