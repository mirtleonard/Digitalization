# Generated by Django 3.2.4 on 2021-08-09 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventReport', '0004_auto_20210809_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreport',
            name='beginingDate',
            field=models.DateTimeField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='eventreport',
            name='endDate',
            field=models.DateTimeField(blank=True, default=datetime.date.today),
        ),
    ]
