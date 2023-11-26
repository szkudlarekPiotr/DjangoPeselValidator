from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import PeselForm, TextForm
import os
from .models import Texts
import random as r
from django.conf import settings


class SavesValidatedPESEL(TestCase):
    def test_short_pesel(self):
        form = PeselForm(data={"pesel_number": "3827193"})
        self.assertFalse(form.is_valid())

    def test_invalid_pesel(self):
        form = PeselForm(data={"pesel_number": "38273625213"})
        self.assertFalse(form.is_valid())

    def test_valid_pesel(self):
        form = PeselForm(data={"pesel_number": os.environ["VALID_PESEL"]})
        self.assertTrue(form.is_valid())


class CanUploadOnlyTxtFiles(TestCase):
    def test_upload_txt_file(self):
        txt_file = SimpleUploadedFile("file.txt", b"Content", content_type="text/plain")
        form = TextForm(files={"file": txt_file})
        self.assertTrue(form.is_valid())

    def test_upload_non_txt_file(self):
        non_txt_file = SimpleUploadedFile(
            "file.jpg",
            content=open(
                f"{settings.MEDIA_ROOT}/test_image/test_image.jpg", "rb"
            ).read(),
            content_type="image/jpg",
        )
        form = TextForm(files={"file": non_txt_file})
        self.assertFalse(form.is_valid())


class ModelShufflesWords(TestCase):
    def setUp(self):
        self.seed = r.seed("234")
        self.inital_word = "shuffled"
        self.test_file = SimpleUploadedFile(
            "initial.txt", b"shuffled", content_type="text/plain"
        )
        self.inital_word_instance = Texts(file=self.test_file)

    def test_shuffles_word(self):
        instance = self.inital_word_instance
        self.assertNotEqual(instance.get_shuffled_text, self.inital_word)

    def test_first_and_last_char(self):
        instance = self.inital_word_instance
        shuffled_text = instance.get_shuffled_text
        self.assertEqual(shuffled_text[0], self.inital_word[0])
        self.assertEqual(shuffled_text[-1], self.inital_word[-1])
