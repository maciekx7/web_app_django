# Generated by Django 2.2.4 on 2019-09-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja_raportowanie', '0004_auto_20190911_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpost',
            name='QM_id',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='QM_id',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
    ]