# Generated by Django 2.2.4 on 2019-09-18 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0007_auto_20190917_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalpost',
            name='modify_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='modify_author',
        ),
    ]
