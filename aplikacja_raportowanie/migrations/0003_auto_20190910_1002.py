# Generated by Django 2.2.4 on 2019-09-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0002_auto_20190909_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpost',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]