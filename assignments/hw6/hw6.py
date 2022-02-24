"""
Name: Calvin Widholm
hw6.py

Problem: Modifying objects in parameters and using strings to do various tasks

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.- I Certify- CW
"""

import math

def cash_converter():
    integer = eval(input("Enter an integer:"))
    print("That is ${:.2f}".format(integer))



def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    length_message = len(message)
    encrypted_message = ""
    for i in range(length_message):
        single_char = message[i]
        encrypt = ord(single_char) + key
        new_char = chr(encrypt)
        encrypted_message = encrypted_message + new_char
    print(encrypted_message)


def sphere_area(radius: float):
    radius_squared = radius * radius
    surface_area = 4 * math.pi * radius_squared
    return surface_area


def sphere_volume(radius: float):
    radius_cubed = radius * radius * radius
    volume = (4/3) * math.pi * radius_cubed
    return volume


def sum_n(number: int):
    summation = 0
    for i in range(1, number + 1):
        summation = summation + i
    return summation


def sum_n_cubes(number: int):
    summation = 0
    for i in range(1, number + 1):
        cubed_term = i ** 3
        summation = summation + cubed_term
    return summation


def encode_better():
    message = input("enter a message:")
    key = input("enter a key word:")
    length_message = len(message)
    length_key = len(key)
    elements = []
    for i in range(length_message):
        elements.append(message[i])
    key_elements = []
    for j in range(length_message):
        key_elements.append(key[j % length_key])
    encrypt_message = []
    for k in range(length_message):
        key_ordinal = ord(key_elements[k]) - 65
        message_ordinal = ord(message[k]) - 65
        encrypt_message_ordinal = (message_ordinal + key_ordinal) % 58
        encrypt_message_char = chr(encrypt_message_ordinal + 65)
        encrypt_message.append(encrypt_message_char)
    final_message = "".join(encrypt_message)
    print(final_message)




if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
