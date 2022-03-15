"""
Name: Calvin Widholm
lab8.py

Problem: Developing a file for a professor using numeric data from a file

Certification of Authenticity:
I certify that this assignment is entirely my own work. I certify- CW
"""

def weighted_average(in_file_name, out_file_name):
    name_list = []
    weight_grade_list = []
    average_list = []
    class_average_list = []
    opened = open(in_file_name, "r")
    for line in opened:
        name_grade_split = line.split(":")
        name = name_grade_split[0]
        name_list.append(name)
        weight_grade = name_grade_split[1]
        new_weight_grade = weight_grade.replace("\n", "")
        weight_grade_list.append(new_weight_grade)
    length_weight_list = len(weight_grade_list)
    for i in range(length_weight_list):
        element = weight_grade_list[i]
        parsed_element = element.lstrip()
        split_element = parsed_element.split(" ")
        accumulator = 0
        weight_accumulator = 0
        for j in range(int(.5 * len(split_element))):
            weight = eval(split_element[2 * j])
            grade = eval(split_element[(2 * j) + 1])
            multiplied = (weight * grade)
            accumulator = accumulator + multiplied
            weight_accumulator = weight_accumulator + weight
        if weight_accumulator == 100:
            average = accumulator / 100
            rounded_average = round(average, 1)
            average_list.append(rounded_average)
            class_average_list.append(rounded_average)
        if weight_accumulator > 100:
            average = "The weights are greater than 100."
            average_list.append(average)
        if weight_accumulator < 100:
            average = "The weights are less than 100."
            average_list.append(average)
    class_average_accumulator = 0
    class_average_length = len(class_average_list)
    for k in range(class_average_length):
        class_contribution = class_average_list[k]
        class_average_accumulator = class_average_accumulator + class_contribution
    class_average = class_average_accumulator / class_average_length
    rounded_class_average = round(class_average, 1)
    output = open(out_file_name, "w")
    for l in range(len(name_list)):
        print(name_list[l] + "'s average:", average_list[l], file= output)
    print("Class average:", rounded_class_average, file= output)

    opened.close()
    output.close()


