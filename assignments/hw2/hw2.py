"""
Name: Calvin Widholm
hw2.py

Problem: Doing various arithmetic problems or using math library

Certification of Authenticity: I certify this is all my own work
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Brett Widholm>- I certify
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    n_series = upper_bound // 3
    fact = 0
    for multiple in range(1, n_series + 1, 1):
        fact = fact + (3 * multiple)
    print(fact)



def multiplication_table():
    for i in range(1,11,1):
        print(end="\n")
        for j in range(1,11,1):
            number = i * j
            print(number, end="\t")



def triangle_area():
    side_a = eval(input("Enter the side a length: "))
    side_b = eval(input("Enter the side b length: "))
    side_c = eval(input("Enter the side c length: "))
    sum_side = (side_a + side_b + side_c) / 2
    area = math.sqrt(sum_side * (sum_side - side_a) * (sum_side - side_b) * (sum_side - side_c))
    print("area is", area)


def sum_squares():
    low_range = eval(input("Enter lower range: "))
    up_range = eval(input("Enter upper range: "))
    fact = 0
    for i in range(low_range, up_range + 1, 1):
        fact = fact + i * i
    print(fact)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    orig_base = base
    for _ in range(1, exponent):
        for j in [orig_base]:
            base = base * j
    print(orig_base, "^", exponent, "=", base)





if __name__ == '__main__':
    pass
