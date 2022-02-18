"""
Name: Calvin Widholm
hw5.py

Problem: Using lists and strings and indexing/slicing them

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.- I certify- CW
"""


def name_reverse():
    name = input("Enter a name (first last):")
    split_name = name.split()
    reverse_a = split_name[1]
    reverse_b = split_name[0]
    print(reverse_a + ",", reverse_b)


def company_name():
    domain = input("Enter a domain:")
    split_domain = domain.split(".")
    company = split_domain[1]
    print(company)


def initials():
    student_num = eval(input("How many students are in the class?"))
    for i in range(1, student_num + 1):
        print("What is the name of student", i, "?")
        student = input()
        split_student = student.split()
        first_name = split_student[0]
        last_name = split_student[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        print(first_initial + last_initial)


def names():
    name_list = input("Enter a list of names:")
    split_names = name_list.split(",")
    initials = []
    for i in split_names:
        split_single_name = i.split()
        first_name = split_single_name[0]
        last_name = split_single_name[1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        combined = first_initial + last_initial
        initials.append(combined)
    string_initials = " ".join(initials)
    print(string_initials)


def thirds():
    sentences = eval(input("Enter the number of sentences"))
    sentence_list = []
    for i in range(1, sentences + 1):
        print("Enter sentence", i)
        submit_sentence = input()
        sentence_length = len(submit_sentence)
        parsed_sentence = submit_sentence[0:sentence_length:3]
        sentence_list.append(parsed_sentence)
    for j in sentence_list:
        print(j)




def word_average():
    sentence = input("Enter a sentence:")
    average = 0
    split_sentence = sentence.split()
    split_list_length = len(split_sentence)
    for i in split_sentence:
        word_length = len(i)
        average = average + word_length
    average_length = average / split_list_length
    print(average_length)


def pig_latin():
    sentence = input("Enter an sentence to convert to pig latin:")
    split_sentence = sentence.split()
    sentence_list = []
    for i in split_sentence:
        length_word = len(i)
        first_letter = i[0]
        rest_of_word = i[1:length_word]
        new_word = rest_of_word + first_letter + "ay"
        lower_new_word = new_word.lower()
        sentence_list.append(lower_new_word)
    print_sentence = " ".join(sentence_list)
    print(print_sentence)




if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
