# Generated by Django 4.2.7 on 2023-11-24 22:41

import ZadaniaRekrutacyjne.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ZadaniaRekrutacyjne", "0005_rename_pesel_peseldata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="texts",
            name="file",
            field=models.FileField(
                upload_to="text_files",
                validators=[ZadaniaRekrutacyjne.validators.validate_file_type],
            ),
        ),
        migrations.AlterField(
            model_name="texts",
            name="scrambled_text",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
