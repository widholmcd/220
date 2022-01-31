"""
Name: Calvin Widholm
hw3.py

Problem: Do various arithmetic- add later

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    num_grades = eval(input("How many grades will you enter?"))
    initial_value = 0
    for i in range(num_grades):
        j = eval(input("Enter grade: "))
        initial_value = initial_value + j
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
    for i in range(num_approx):
        approx = ((approx + (x_value / approx)) / 2)
    print("The square root is approximately ", approx)



def sequence():
    terms = eval(input("How many terms would you like?"))
    for j in range(1, terms + 1):
        print(2 * round((j + .01) / 2) - 1)


    #Come back to we need to resolve odd terms issue



def pi():
    pass
   # terms = eval(input("How many terms in the series?"))
   # for b in range(1, 1 + terms, 2):
      #  for a in range(2, 1 + terms, 2):

   # for i in range(terms):



if __name__ == '__main__':
    pass
