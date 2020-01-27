# task 4
from functools import reduce


def is_right_by_luhn(str_number="") -> bool:
    if str_number is None or str_number == "":
        return False

    try:
        # change str to int
        parsed_num_int = list(map(int, str_number.replace(" ", "")))
        odds = parsed_num_int[-1::-2]  # reverse and take every 2nd digit start from last
        evens = parsed_num_int[-2::-2]  # reverse and take every 2nd digit start from last - 1

        evens_new = list(map((lambda x: x * 2 if x * 2 < 10 else x * 2 - 9), evens))
        evens_sum = reduce((lambda x, y: x + y), evens_new)
        odds_sum = reduce((lambda x, y: x + y), odds)

        return (evens_sum + odds_sum) % 10 == 0
    except ValueError:
        print('Input array cannot be parsed to digits!')
        return False


# Check algorithm

# 49927398716 VALID
print('49927398716 is fine: ', is_right_by_luhn('49927398716'))
# 49927398717 INVALID
print('49927398717 is fine: ', is_right_by_luhn('49927398717'))
# 1234567812345678 INVALID
print('1234567812345678 is fine: ', is_right_by_luhn('1234567812345678'))
# 1234567812345670 VALID
print('1234567812345670 is fine: ', is_right_by_luhn('1234567812345670'))
# 4561 2612 1234 5467 VALID
print('4561 2612 1234 5467 is fine: ', is_right_by_luhn('4561 2612 1234 5467'))
# 4561 2612 1234 5464 INVALID
print('4561 2612 1234 5464 is fine: ', is_right_by_luhn('4561 2612 1234 5464'))
