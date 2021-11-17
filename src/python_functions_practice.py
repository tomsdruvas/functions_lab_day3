def return_10():
    return 10


def add(numb1, numb2):
    return numb1 + numb2

def subtract(numb1, numb2):
    return numb1 - numb2

def multiply(numb1, numb2):
    return numb1 * numb2

def divide(numb1, numb2):
    return numb1 // numb2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(numb1, numb2):
    return int(numb1) + int(numb2)


def number_to_full_month_name(numb1):
    import calendar
    return calendar.month_name[numb1]

def number_to_short_month_name(numb1):
    import calendar
    return calendar.month_abbr[numb1]


def volume(numb1, numb2, numb3):
    return numb1 * numb2 * numb3

def reverse_string(string):
    return string[::-1]

def convert_temp(x_f):
    return (x_f - 32) * 5 // 9
