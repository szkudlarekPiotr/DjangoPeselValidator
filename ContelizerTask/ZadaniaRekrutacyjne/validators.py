from django.core.exceptions import ValidationError
import datetime

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def correct_pesel_date(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900
    try:
        date = datetime.datetime(year=year, month=month, day=day)
    except ValueError:
        return False
    else:
        return True


def count_pesel_control(pesel):
    multiplied_pesel = []
    for x in range(0, len(WEIGHTS)):
        multiplied_pesel.append(pesel[x] * WEIGHTS[x])
    stripped_weights = [num % 10 if num > 10 else num for num in multiplied_pesel]
    if sum(stripped_weights) > 10:
        control_number = 10 - sum(stripped_weights) % 10
    return control_number


def validate_pesel(pesel):
    numbers_list = [int(num) for num in pesel]
    if len(numbers_list) < 11:
        raise ValidationError("Your PESEL number is too short")
    if count_pesel_control(numbers_list) != numbers_list[-1] or not correct_pesel_date(
        pesel
    ):
        raise ValidationError(f"Your PESEL number is invalid.")
