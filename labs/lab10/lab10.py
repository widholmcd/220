"""
Name: Calvin Widholm
button.py

Problem: Creating a graphics window where the door if clicked opens or closes, it is updated, exit button for exit.

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I certify- CW
"""

from button import Button
from door import Door
from graphics import Point, Rectangle, GraphWin

def main():
    #Graphics Window
    win = GraphWin('test', 700, 700)

    #Button Building
    button_rec_point_1 = Point(200, 25)
    button_rec_point_2 = Point(500, 150)
    my_button = Rectangle(button_rec_point_1, button_rec_point_2)
    button_label = "Exit"

    #Door Building
    door_rec_point_1 = Point(200, 200)
    door_rec_point_2 = Point(500, 700)
    my_door = Rectangle(door_rec_point_1, door_rec_point_2)
    door_label = 'Closed'

    #Button and Door Constructors
    button = Button(my_button, button_label)
    door = Door(my_door, door_label)

    #Drawing on win
    button.draw(win)
    door.draw(win)

    #Coloring Respectives
    button.color_button("gray")
    door_color = 'red'
    door.color(door_color)

    #Door Loop
    click = Point(0,0)
    while not button.is_clicked(click):
        click = win.getMouse()
        if door_color == 'red':
            secret = True
            door.set_secret(secret)
        else:
            secret = False
            door.set_secret(secret)
        if door.is_clicked(click):
            if door.is_secret():
                door_color = 'white'
                door_label = 'Open'
                door.open(door_color, door_label)
            else:
                door_color = 'red'
                door_label = 'Closed'
                door.close(door_color, door_label)
    win.close()
