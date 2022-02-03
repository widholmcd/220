"""
Name: Calvin Widholm
hw3.py

Problem: Do various arithmetic problems with loops and generating sequences with loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.- Calvin Widholm (I certify)
"""


def average():
    num_grades = eval(input("How many grades will you enter?"))
    initial_value = 0
    for _ in range(num_grades):
        grade = eval(input("Enter grade: "))
        initial_value = initial_value + grade
    avg_num = initial_value / num_grades
    print("average is", avg_num)


def tip_jar():
    tip_1 = eval(input("How much would you like to donate?"))
    tip_2 = eval(input("How much would you like to donate?"))
    tip_3 = eval(input("How much would you like to donate?"))
    tip_4 = eval(input("How much would you like to donate?"))
    tip_5 = eval(input("How much would you like to donate?"))
    total_tips = tip_1 + tip_2 + tip_3 + tip_4 + tip_5
    print("total tips:", total_tips)


def newton():
    x_value = eval(input("What number do you want to square root?"))
    num_approx = eval(input("How many times should we improve the approximation?"))
    approx = x_value
    for _ in range(num_approx):
        approx = ((approx + (x_value / approx)) / 2)
    print("The square root is approximately ", approx)



def sequence():
    terms = eval(input("How many terms would you like?"))
    for j in range(1, terms + 1):
        print(2 * round((j + .01) / 2) - 1)


def pi():
    terms = eval(input("How many terms in the series?"))
    pi_over_2_approx = 1
    for i in range(1, terms + 1, 1):
        numerator = (2 * round((i + .01) / 2))
        denominator = (2 * round((i + 1.01) / 2)) - 1
        pi_solve = (numerator / denominator)
        pi_over_2_approx = pi_over_2_approx * pi_solve
    pi_approx = 2 * pi_over_2_approx
    print(pi_approx)


if __name__ == '__main__':
    pass
