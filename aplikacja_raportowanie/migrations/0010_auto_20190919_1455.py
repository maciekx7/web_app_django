# Generated by Django 2.2.4 on 2019-09-19 14:55

import aplikacja_raportowanie.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0009_auto_20190919_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpost',
            name='file',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[aplikacja_raportowanie.validators.validate_file_size, django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'png', 'txt'])]),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[aplikacja_raportowanie.validators.validate_file_size, django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'png', 'txt'])]),
        ),
    ]
