"""
Name: Calvin Widholm
hw10.py

Problem: Using loops and bools to obtain various abstract math concepts and creating class methods

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""

from graphics import GraphWin, Point
from face import Face

def fibonacci(n_term:int):
    fibo_list = [0, 1]
    count = 0
    while count <= n_term:
        count += 1
        fibo_term = fibo_list[count] + fibo_list[count - 1]
        fibo_list.append(fibo_term)
    if n_term >= 1:
        if n_term == 1:
            return 1
        return fibo_list[count - 1]
    if n_term < 1:
        return None

def double_investment(principle:float, rate:float):
    year_count = 0
    total = principle
    while total < (2 * principle):
        total = total * (1 + rate)
        year_count += 1
    return year_count

def syracuse(n_term:int):
    syracuse_list = []
    syracuse_list.append(n_term)
    if n_term < 1:
        return None
    while n_term != 1:
        if (2 * (n_term // 2) + 1) == n_term:
            n_term = int((3 * n_term) + 1)
        elif (2 * (n_term // 2)) == n_term:
            n_term = int(n_term / 2)
        syracuse_list.append(n_term)
    return syracuse_list

def is_prime(n_term:int):
    count = 2
    while count < n_term:
        if n_term % count == 0:
            return False
        count += 1
    return True


def goldbach(n_term:int):
    prime_list = []
    first_prime_list = []
    second_prime_list = []
    conjecture_list = []

    if (2 * (n_term // 2)) + 1 == n_term:
        return None
    if (2 * (n_term // 2)) == n_term:
        count = 2
        while count < n_term:
            if is_prime(count):
                prime_list.append(count)
            count += 1
        first_count = 0
        second_count = 0
        while first_count < len(prime_list):
            first_prime_list.append(prime_list[first_count])
            first_count += 1
        while second_count < len(prime_list):
            second_prime_list.append(prime_list[second_count])
            second_count += 1
        first_count = 0
        while first_count < len(first_prime_list):
            second_count = 0
            while second_count < len(second_prime_list):
                if (first_prime_list[first_count] + second_prime_list[second_count]) == n_term:
                    conjecture_list.append(first_prime_list[first_count])
                    conjecture_list.append(second_prime_list[second_count])
                    return conjecture_list
                second_count += 1
            first_count += 1

#testing all methods from face class
def face_test_1():
    window = GraphWin('test', 700, 700)
    center = Point(350, 350)
    size = 100
    face = Face(window, center, size)
    face.smile()
    window.getMouse()
    window.close()

def face_test_2():
    window = GraphWin('test', 700, 700)
    center = Point(350, 350)
    size = 100
    face = Face(window, center, size)
    face.shock()
    window.getMouse()
    window.close()

def face_test_3():
    window = GraphWin('test', 700, 700)
    center = Point(350, 350)
    size = 100
    face = Face(window, center, size)
    face.wink()
    window.getMouse()
    window.close()
