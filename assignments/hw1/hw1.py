"""
Name: Calvin Widholm
<hw1>.py

Problem: <This program calculates basic arithmetic problems using user input numbers.>

Certification of Authenticity:
<This is my own work, but I did discuss what a file is and how to test the code I write
while I was out due to Covid protocol>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Brett Widholm>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume is =", volume)


def shooting_percentage():
    total_shot = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enther how many shots the player made: "))
    shot_percent_decimal = shots_made / total_shot
    shot_percentage = shot_percent_decimal * 100
    print("Shooting Percentage:", shot_percentage, "%")


def coffee():
    coffee_pounds = eval(input("How many pounds of coffee would you  like? "))
    coffee_pounds_price = coffee_pounds * 10.5
    coffee_pounds_price_shipping = coffee_pounds * .86
    total_coffee_cost = 1.5 + (coffee_pounds_price + coffee_pounds_price_shipping)
    print("Your total is:","$", total_coffee_cost)


def kilometers_to_miles():
    kilometers_traveled = eval(input("How many kilometers did you travel? "))
    miles_traveled = kilometers_traveled / 1.61
    print("That's", miles_traveled, "miles!")


if __name__ == '__main__':
    pass
