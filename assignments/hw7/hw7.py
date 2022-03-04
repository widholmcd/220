"""
Name: Calvin Widholm
hw7.py

Problem: Writing functions while also reading and writing files

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brett Widholm- CW
For clarity- I discussed with Brett: the rstip method (I did not look at code for this)
"""

from encryption import encode, encode_better


def number_words(in_file_name: str, out_file_name: str):
    opened = open(in_file_name, "r")
    words = opened.read()
    modified_words = words.rstrip()
    one_line = modified_words.replace("\n", " ")
    split_words = one_line.split(" ")
    output_file = open(out_file_name, "w")
    for i in range(1, len(split_words) + 1):
        print(i, split_words[i - 1], file=output_file)

def hourly_wages(in_file_name: str, out_file_name: str):
    first_name_list = []
    last_name_list = []
    wage_list = []
    hours_worked_list = []
    bonus_list = []
    base_pay_list = []
    total_pay_list = []
    opened = open(in_file_name, "r")
    for line in opened:
        split_line = line.split(" ")
        first_name = split_line[0]
        first_name_list.append(first_name)
        last_name = split_line [1]
        last_name_list.append(last_name)
        wage = split_line[2]
        wage_list.append(wage)
        hours = split_line[3]
        hours_modify = hours.replace("\n", "")
        hours_worked_list.append(hours_modify)
    length_hours = len(hours_worked_list)
    for i in range(length_hours):
        hour = hours_worked_list[i]
        bonus = eval(hour) * 1.65
        bonus_list.append(bonus)
    for j in range(length_hours):
        base_pay = eval(hours_worked_list[j]) * eval(wage_list[j])
        base_pay_list.append(base_pay)
    for k in range(length_hours):
        total_pay = base_pay_list[k] + bonus_list[k]
        string_pay = "{:.2f}".format(total_pay)
        total_pay_list.append(string_pay)
    output = open(out_file_name, "w")
    for l in range(length_hours):
        print(first_name_list[l], last_name_list[l], total_pay_list[l], file=output)


def calc_check_sum(isbn: str):
    new_isbn = isbn.replace("-", "")
    start = 0
    for i in range(10, len(new_isbn) -10, -1):
        start = start + (eval(new_isbn[-i]) * i)
    return start



def send_message(file_name: str, friend_name: str):
    opened = open(file_name)
    data = opened.read()
    modified_data = data.rstrip()
    output = open(friend_name + ".txt", "w")
    print(modified_data, file=output)



def send_safe_message(file_name: str, friend_name: str, key: int):
    encode_list = []
    opened = open(file_name, "r")
    for line in opened:
        no_more_spaces = line.rstrip()
        encoded_message = encode(no_more_spaces, key)
        encode_list.append(encoded_message)
    output = open(friend_name + ".txt", "w")
    for i in range(len(encode_list)):
        print(encode_list[i], file=output)



def send_uncrackable_message(file_name: str, friend_name: str, pad_file_name: str):
    opened = open(file_name, "r")
    words = opened.read()
    opened_2 = open(pad_file_name, "r")
    words_2 = opened_2.read()
    encrypted_message = encode_better(words, words_2)
    output = open(friend_name + ".txt", "w")
    print(encrypted_message, file=output)




if __name__ == '__main__':
    pass
