"""
Name: Calvin Widholm
lab11.py

Problem: Creating a 3 door game where user guesses which door is the right one

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from lab10.door import Door
from lab10.button import Button
from random import randint
from graphics import GraphWin, Point, Rectangle, Text


def three_door_game():
    # Graphics Window
    win = GraphWin('3 Door Game', 700, 700)

    # Button Building
    button_rec_point_1 = Point(500, 25)
    button_rec_point_2 = Point(650, 100)
    my_button = Rectangle(button_rec_point_1, button_rec_point_2)
    button_label = "Quit"

    # Door 1 Building
    door_1_rec_point_1 = Point(75, 200)
    door_1_rec_point_2 = Point(225, 600)
    my_door_1 = Rectangle(door_1_rec_point_1, door_1_rec_point_2)
    door_1_label = 'Door 1'

    # Door 2 Building
    door_2_rec_point_1 = Point(275, 200)
    door_2_rec_point_2 = Point(425, 600)
    my_door_2 = Rectangle(door_2_rec_point_1, door_2_rec_point_2)
    door_2_label = 'Door 2'

    # Door 3 Building
    door_3_rec_point_1 = Point(475, 200)
    door_3_rec_point_2 = Point(625, 600)
    my_door_3 = Rectangle(door_3_rec_point_1, door_3_rec_point_2)
    door_3_label = 'Door 3'

    # Button and Door Constructors
    button = Button(my_button, button_label)
    door_1 = Door(my_door_1, door_1_label)
    door_2 = Door(my_door_2, door_2_label)
    door_3 = Door(my_door_3, door_3_label)

    # Drawing on win
    button.draw(win)
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    # Coloring Respectives
    button.color_button("gray")
    door_1_color = 'chocolate4'
    door_2_color = 'chocolate4'
    door_3_color = 'chocolate4'
    door_1.color(door_1_color)
    door_2.color(door_2_color)
    door_3.color(door_3_color)

    # Selecting The Chosen Door
    random_door = randint(1, 3)
    if random_door == 1:
        door_1.set_secret(True)
    if random_door == 2:
        door_2.set_secret(True)
    if random_door == 3:
        door_3.set_secret(True)

    # Win and Lose Lists
    win_list = []
    lose_list = []

    # Win Loss Counter
    win_rectangle_point_1 = Point(75, 50)
    win_rectangle_point_2 = Point(150, 125)
    win_box = Rectangle(win_rectangle_point_1, win_rectangle_point_2)
    win_box.draw(win)
    win_text = Text(Point(112.5, 40), 'Wins')
    win_text.draw(win)


    loss_rectangle_point_1 = Point(150, 50)
    loss_rectangle_point_2 = Point(225, 125)
    loss_box = Rectangle(loss_rectangle_point_1, loss_rectangle_point_2)
    loss_box.draw(win)
    loss_text = Text(Point(187.5, 40), 'Losses')
    loss_text.draw(win)

    #Game Loop
    click = Point(0, 0)
    win_number = Text(Point(112.5, 87.5), '')
    win_number.draw(win)
    win_number.setText(len(win_list))
    loss_number = Text(Point(187.5, 87.5), '')
    loss_number.draw(win)
    loss_number.setText(len(lose_list))
    while not button.is_clicked(click):
        instructions_1 = Text(Point(350, 125), 'I have a secret door')
        instructions_1.draw(win)
        instructions_2 = Text(Point(350, 625), 'Click to guess which is the secret door!')
        instructions_2.draw(win)
        click = win.getMouse()
        if door_1.is_clicked(click):
            if door_1.is_secret():
                door_1.color('green')
                instructions_1.undraw()
                winning_remark = Text(Point(350, 125), 'You Win!')
                winning_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_remark.undraw()
                new_instructions.undraw()
            else:
                door_1.color('red')
                if door_2.is_secret():
                    door_2.color('green')
                if door_3.is_secret():
                    door_3.color('green')
                instructions_1.undraw()
                losing_remark = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_remark.undraw()
                new_instructions.undraw()

        elif door_2.is_clicked(click):
            if door_2.is_secret():
                door_2.color('green')
                instructions_1.undraw()
                winning_remark = Text(Point(350, 125), 'You Win!')
                winning_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_remark.undraw()
                new_instructions.undraw()
            else:
                door_2.color('red')
                if door_1.is_secret():
                    door_1.color('green')
                if door_3.is_secret():
                    door_3.color('green')
                instructions_1.undraw()
                losing_remark = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_remark.undraw()
                new_instructions.undraw()

        elif door_3.is_clicked(click):
            if door_3.is_secret():
                door_3.color('green')
                instructions_1.undraw()
                winning_remark = Text(Point(350, 125), 'You Win!')
                winning_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_remark.undraw()
                new_instructions.undraw()
            else:
                door_3.color('red')
                if door_1.is_secret():
                    door_1.color('green')
                if door_2.is_secret():
                    door_2.color('green')
                instructions_1.undraw()
                losing_remark = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_remark.draw(win)
                instructions_2.undraw()
                new_instructions = Text(Point(350, 625), 'Click anywhere to play again')
                new_instructions.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_remark.undraw()
                new_instructions.undraw()
        elif (not door_1.is_clicked(click)) and (not door_2.is_clicked(click)) and (not door_3.is_clicked(click)):
            instructions_1.undraw()
            instructions_2.undraw()

        door_1.color('chocolate4')
        door_2.color('chocolate4')
        door_3.color('chocolate4')
        door_1.set_secret(False)
        door_2.set_secret(False)
        door_3.set_secret(False)
        random_door = randint(1, 3)
        if random_door == 1:
            door_1.set_secret(True)
        if random_door == 2:
            door_2.set_secret(True)
        if random_door == 3:
            door_3.set_secret(True)

    win.close()



