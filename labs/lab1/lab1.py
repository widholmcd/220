"""
Calvin Widholm
lab1.py

Problem Description: Calculate the monthly interest charge with respect to user inputs of an annual interest rate,
number of days in billing cycle, previous balance, payment amount, and days of cycle when payment was made

Certification of Authenticity:
I certify that this assignment is entirely my own work.- Calvin Widholm
"""

def monthly_interest_rate():
    annual_interest = eval(input("Enter the annual interest rate as a percent, excluding the percent sign: "))
    days_in_billing = eval(input("Enter the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter your previous balance: $ "))
    payment_amount = eval(input("Enter the payment amount: $ "))
    payment_day = eval(input("Enter the day of cycle when the payment was made, as a number: "))

    dec_annual_interest = annual_interest / 100

    balance_x_days_in_billing = previous_balance * days_in_billing
    days_before_cycle_ends = days_in_billing - payment_day
    payment_amount_x_days_before_cycle_ends = payment_amount * days_before_cycle_ends
    payment_amount_x_days_minus_balance_x_days = balance_x_days_in_billing - payment_amount_x_days_before_cycle_ends
    average_daily_balance = payment_amount_x_days_minus_balance_x_days / days_in_billing

    calculated_monthly_rate = dec_annual_interest / 12

    monthly_interest_charge = average_daily_balance * calculated_monthly_rate
    displayed_monthly_interest_charge = round(monthly_interest_charge, 2)

    print("Your monthly interest charge is: $", displayed_monthly_interest_charge)

