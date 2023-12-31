# Generated by Django 4.2.7 on 2023-11-24 20:45

import ZadaniaRekrutacyjne.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ZadaniaRekrutacyjne", "0003_alter_pesel_pesel_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="pesel",
            name="birthdate",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="pesel",
            name="sex",
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name="pesel",
            name="pesel_number",
            field=models.CharField(
                max_length=11,
                validators=[ZadaniaRekrutacyjne.validators.validate_pesel],
            ),
        ),
    ]
