from django.db import models
import datetime
from .validators import validate_pesel, validate_file_type
from .utils import extract_birthdate
import string
import random as r


class Texts(models.Model):
    file = models.FileField(upload_to="text_files", validators=[validate_file_type])
    shuffled_text = models.CharField(null=True)

    @property
    def get_shuffled_text(self):
        content = self.file.open().read().decode("utf-8").splitlines()
        split_content = [
            word.strip(string.punctuation)
            for line in content
            if line
            for word in line.split(" ")
            if word
        ]
        shuffled_content = []
        for item in split_content:
            if len(item) > 3:
                shuffled_content.append(
                    item[0] + "".join(r.sample(item[1:-1], len(item[1:-1]))) + item[-1],
                )
            else:
                shuffled_content.append(item)
        return " ".join(shuffled_content)

    def save(self, *args, **kwargs):
        self.shuffled_text = self.get_shuffled_text
        super(Texts, self).save(*args, **kwargs)


class PeselData(models.Model):
    pesel_number = models.CharField(max_length=11, validators=[validate_pesel])
    birthdate = models.DateField(null=True)
    sex = models.CharField(null=True)

    @property
    def get_birthdate(self):
        pesel = self.pesel_number
        birthdate = datetime.date(*extract_birthdate(pesel))
        return birthdate

    @property
    def get_sex(self):
        pesel = self.pesel_number
        return "female" if int(pesel[-2]) % 2 == 0 else "male"

    def save(self, *args, **kwargs):
        self.birthdate = self.get_birthdate
        self.sex = self.get_sex
        super(PeselData, self).save(*args, **kwargs)
