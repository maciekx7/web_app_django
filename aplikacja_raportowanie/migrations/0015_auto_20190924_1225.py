# Generated by Django 2.2.4 on 2019-09-24 12:25

import aplikacja_raportowanie.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0014_auto_20190923_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('nowy', 'nowy'), ('do podjęcia', 'do podjęcia'), ('w obserwacji', 'w obserwacji'), ('wstrzymane', 'wstrzymane'), ('przekazane', 'przekazane'), ('w realizacji', 'w realizacji'), ('zamknięte', 'zamknięte')], max_length=15),
        ),
        migrations.AlterField(
            model_name='historicalcomment',
            name='status',
            field=models.CharField(choices=[('nowy', 'nowy'), ('do podjęcia', 'do podjęcia'), ('w obserwacji', 'w obserwacji'), ('wstrzymane', 'wstrzymane'), ('przekazane', 'przekazane'), ('w realizacji', 'w realizacji'), ('zamknięte', 'zamknięte')], max_length=15),
        ),
        migrations.AlterField(
            model_name='historicalpost',
            name='file',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[aplikacja_raportowanie.validators.validate_file_size, django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'txt', 'doc', 'docx', 'dot', 'docm', 'dotm', 'xml', 'odt', 'dotx', 'xls', 'xlsx', 'xlsb', 'xslm', 'xltx', 'xlt', 'ods', 'ppt', 'pptx', 'potx', 'pot', 'odp', 'pps', 'ppsx', 'pptm', 'potm', 'ppsm'])]),
        ),
        migrations.AlterField(
            model_name='historicalpost',
            name='status',
            field=models.CharField(choices=[('nowy', 'nowy'), ('do podjęcia', 'do podjęcia'), ('w obserwacji', 'w obserwacji'), ('wstrzymane', 'wstrzymane'), ('przekazane', 'przekazane'), ('w realizacji', 'w realizacji'), ('zamknięte', 'zamknięte')], default='nowy', max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[aplikacja_raportowanie.validators.validate_file_size, django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp', 'txt', 'doc', 'docx', 'dot', 'docm', 'dotm', 'xml', 'odt', 'dotx', 'xls', 'xlsx', 'xlsb', 'xslm', 'xltx', 'xlt', 'ods', 'ppt', 'pptx', 'potx', 'pot', 'odp', 'pps', 'ppsx', 'pptm', 'potm', 'ppsm'])]),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('nowy', 'nowy'), ('do podjęcia', 'do podjęcia'), ('w obserwacji', 'w obserwacji'), ('wstrzymane', 'wstrzymane'), ('przekazane', 'przekazane'), ('w realizacji', 'w realizacji'), ('zamknięte', 'zamknięte')], default='nowy', max_length=15),
        ),
    ]
