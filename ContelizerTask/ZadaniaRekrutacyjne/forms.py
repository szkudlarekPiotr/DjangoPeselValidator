from django.forms import ModelForm
from .models import Texts, PeselData


class TextForm(ModelForm):
    class Meta:
        model = Texts
        fields = ["file"]


class PeselForm(ModelForm):
    class Meta:
        model = PeselData
        fields = ["pesel_number"]
