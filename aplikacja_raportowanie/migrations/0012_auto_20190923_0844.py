# Generated by Django 2.2.4 on 2019-09-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0011_auto_20190919_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpost',
            name='tictet_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tictet_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
