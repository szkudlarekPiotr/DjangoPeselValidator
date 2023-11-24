from django.db import models
from .validators import validate_pesel
import datetime


class Texts(models.Model):
    file = models.FileField(upload_to="text_files")
    scrambled_text = models.CharField(max_length=50)


class PeselData(models.Model):
    pesel_number = models.CharField(max_length=11, validators=[validate_pesel])
    birthdate = models.DateField(null=True)
    sex = models.CharField(null=True)

    @property
    def get_birthdate(self):
        pesel = self.pesel_number
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
            date = datetime.date(year=year, month=month, day=day)
        except ValueError:
            return False
        return date

    @property
    def get_sex(self):
        pesel = self.pesel_number
        if int(pesel[-2]) % 2 == 0:
            return "female"
        return "male"

    def save(self, *args, **kwargs):
        self.birthdate = self.get_birthdate
        self.sex = self.get_sex
        super(PeselData, self).save(*args, **kwargs)
