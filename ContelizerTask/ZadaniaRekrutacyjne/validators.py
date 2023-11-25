from django.core.exceptions import ValidationError
import datetime
import magic
from .utils import extract_birthadate

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def correct_pesel_date(pesel):
    year, month, day = extract_birthadate(pesel)
    try:
        date = datetime.date(year=year, month=month, day=day)
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


def validate_file_type(file):
    filetype = magic.from_buffer(file.read(), mime=True)
    if not "text/plain" in filetype:
        raise ValidationError("Invalid file type")
