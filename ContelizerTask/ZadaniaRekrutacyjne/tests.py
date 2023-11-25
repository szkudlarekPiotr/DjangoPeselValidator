from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PeselForm, TextForm
import os
from .models import Texts
import random as r
from django.conf import settings


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


class CanUploadOnlyTxtFiles(TestCase):
    def setUp(self):
        self.txt_file = SimpleUploadedFile(
            "file.txt", b"Content", content_type="text/plain"
        )
        self.non_txt_file = SimpleUploadedFile(
            "file.jpg",
            content=open(
                f"{settings.MEDIA_ROOT}/test_image/test_image.jpg", "rb"
            ).read(),
            content_type="image/jpg",
        )

    def test_upload_txt_file(self):
        form = TextForm(files={"file": self.txt_file})
        self.assertTrue(form.is_valid())

    def test_upload_non_txt_file(self):
        form = TextForm(files={"file": self.non_txt_file})
        self.assertFalse(form.is_valid())


class ModelShufflesWords(TestCase):
    def setUp(self):
        self.seed = r.seed("234")
        self.inital_word = "shuffle"
        self.test_file = SimpleUploadedFile(
            "initial.txt", b"shuffle", content_type="text/plain"
        )
        self.shuffled_word = (
            self.inital_word[0]
            + "".join(r.sample(self.inital_word[1:-1], len(self.inital_word[1:-1])))
            + self.inital_word[-1]
        )
        self.inital_word_instance = Texts(file=self.test_file)

    def test_shuffles_word(self):
        instance = self.inital_word_instance
        r.seed("234")
        self.assertEqual(instance.get_shuffled_text, self.shuffled_word)

    def test_doesnt_shuffle(self):
        instance = self.inital_word_instance
        r.seed("234")
        self.assertNotEqual(instance.get_shuffled_text, self.inital_word)
