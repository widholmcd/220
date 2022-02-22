"""
Name: Calvin Widholm
lab6.py

Problem: Creating a vigenere encryption with user input of a message and keyword

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from graphics import GraphWin, Rectangle, Text, Entry, Point

def Vigenere():
    win = GraphWin("Vigenere", 700, 700)
    button = Rectangle(Point(250, 400), Point(450, 300))
    button.draw(win)
    center_botton = button.getCenter()
    button_text = Text(center_botton, "Encode")
    button_text.draw(win)

    message_directions = Text(Point(100, 75), "Message to Encode:")
    message_directions.draw(win)
    key_directions = Text(Point(100, 125), "Enter Keyword:")
    key_directions.draw(win)

    message_entry = Entry(Point(350, 75), 35)
    message_entry.draw(win)
    key_entry = Entry(Point(350, 125), 35)
    key_entry.draw(win)

    win.getMouse()
    message = message_entry.getText()
    key = key_entry.getText()
    edited_message = message.upper()
    parsed_message = edited_message.replace(" ","")
    edited_key = key.upper()
    length_message = len(parsed_message)
    length_key = len(edited_key)

    message_elements = []
    for i in range(length_message):
        message_elements.append(parsed_message[i])
    key_elements = []
    for j in range(length_message):
        key_elements.append(edited_key[j % length_key])
    encrypt_message = []
    for k in range(length_message):
        key_ordinal = ord(key_elements[k]) - 65
        message_ordinal = ord(message_elements[k]) - 65
        encrypt_message_ordinal = (key_ordinal + message_ordinal) % 26
        encrypt_message_char = chr(encrypt_message_ordinal + 65)
        encrypt_message.append(encrypt_message_char)
    final_message = "".join(encrypt_message)

    button.undraw()
    button_text.undraw()

    resulting_message_text = Text(Point(350,350), "Resulting Message")
    resulting_message_text.draw(win)
    encrypted_text = Text(Point(350, 375), final_message)
    encrypted_text.draw(win)

    closing_text = Text(Point(350, 650), "Click once to close window")
    closing_text.draw(win)

    win.getMouse()
    win.close()