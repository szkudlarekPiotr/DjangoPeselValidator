from django.forms import ModelForm
from .models import Texts, Pesel


class TextForm(ModelForm):
    class Meta:
        model = Texts
        fields = ["file"]


class PeselForm(ModelForm):
    class Meta:
        model = Pesel
        fields = ["pesel_number"]
