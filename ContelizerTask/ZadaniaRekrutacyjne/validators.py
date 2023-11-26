from django.core.exceptions import ValidationError
import magic
from .utils import correct_pesel_date, count_pesel_control


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
