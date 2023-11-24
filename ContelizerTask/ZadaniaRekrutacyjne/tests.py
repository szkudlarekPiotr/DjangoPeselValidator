from django.test import TestCase
from django.test import Client
from .forms import PeselForm
import os


class SavesValidatedPESEL(TestCase):
    def setUp(self):
        self.valid_pesel = {"pesel_number": os.environ["OWN_PESEL"]}
        self.short_pesel = {"pesel_number": "0083647382"}
        self.invalid_pesel = {"pesel_number": "84638202932"}

    def test_short_pesel(self):
        form = PeselForm(data=self.short_pesel)
        self.assertFalse(form.is_valid())

    def test_invalid_pesel(self):
        form = PeselForm(data=self.invalid_pesel)
        self.assertFalse(form.is_valid())

    def test_valid_pesel(self):
        form = PeselForm(data=self.valid_pesel)
        self.assertTrue(form.is_valid())
