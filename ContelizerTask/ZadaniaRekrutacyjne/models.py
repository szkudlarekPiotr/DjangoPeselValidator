from django.db import models
from .validators import validate_pesel


class Texts(models.Model):
    file = models.FileField(upload_to="text_files")
    scrambled_text = models.CharField(max_length=50)


class Pesel(models.Model):
    pesel_number = models.IntegerField(validators=[validate_pesel])
