"Calvin Widholm"
"lab2.py"

"Description of problem: We calculate various means depending on how many values "
"the user wants to use"

"Certificate of Authenticity: I certify this is my own work with the help of the lab instructors "
"with list and appending lists"


def means():
    n = eval(input("How many values do you wish to use? "))
    list_general = []
    list_rms = []
    list_harmonic = []
    for i in range(n):
        i = eval(input("Enter value: "))
        list_general.append(i)
        list_rms.append(i * i)
        list_harmonic.append(1/i)

    #Looking at Root-Mean-Square (RMS)
    rms_numerator = sum(list_rms)
    rms_fraction = rms_numerator / n
    rms_average = (rms_fraction) ** .5
    round_rms_average = round(rms_average, 3)
    print("Your rounded Root-Mean-Square is: ", round_rms_average)

    #looking at Harmonic Mean
    h_mean_denom = sum(list_harmonic)
    h_mean = n / h_mean_denom
    round_h_mean = round(h_mean, 3)
    print("Your rounded Harmonic Mean is: ", round_h_mean)

    #looking at Geometric Mean
    g_mean_inside = 1
    for j in list_general:
        g_mean_inside = j * g_mean_inside
    g_mean = g_mean_inside ** (1/n)
    round_g_mean = round(g_mean, 3)
    print("Your rounded Geometric Mean is: ", round_g_mean)

