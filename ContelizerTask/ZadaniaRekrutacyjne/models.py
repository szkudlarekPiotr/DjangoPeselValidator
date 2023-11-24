from django.db import models
from .validators import validate_pesel
from django.core.validators import MinLengthValidator


class Texts(models.Model):
    file = models.FileField(upload_to="text_files")
    scrambled_text = models.CharField(max_length=50)


class Pesel(models.Model):
    pesel_number = models.CharField(max_length=11, validators=[validate_pesel])
