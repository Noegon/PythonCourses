# task 1
def is_leap(year: int) -> bool:
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            return year % 400 == 0


is_error = True

while is_error:
    input_result = input('Insert a year: ')
    try:
        print(input_result + ' year is ' + ('leap' if is_leap(int(input_result)) else 'not leap'))
        is_error = False
    except ValueError:
        print('Please, insert year as integer number')
        is_error = True
