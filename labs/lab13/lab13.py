"""
Name: Calvin Widholm
lab13.py

Problem: Checking signals to see if they quantify as neutron star pulses and stopping search after 5 pulses
or data ends

Certification of Authenticity:
I certify that this assignment is entirely my own work.- I Certify- CW
"""


def star_find(filename):
    opened = open(filename, 'r')
    pulses = opened.read()
    split_pulses = pulses.split(' ')
    strong_pulse_list = []
    strong_pulse_count = 0
    total_pulse_count = 0
    for i in range(len(split_pulses)):
        signal = split_pulses[i]
        eval_signal = eval(signal)
        if 4000 <= eval_signal <= 5000:
            strong_pulse_count += 1
            strong_pulse_list.append(eval_signal)
            total_pulse_count += 1
        else:
            total_pulse_count += 1
        if strong_pulse_count == 5:
            break
    print("The total number of strong pulses found was:", strong_pulse_count)
    for j in range(1, len(strong_pulse_list) + 1):
        print("The strength of pulse", j, 'was:', strong_pulse_list[j - 1])
    if strong_pulse_count == 5:
        print("It took", total_pulse_count, 'signals checked before finding our 5th signal')
    opened.close()
