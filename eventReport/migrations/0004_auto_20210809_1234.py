# Generated by Django 3.2.4 on 2021-08-09 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventReport', '0003_alter_eventreport_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreport',
            name='beginingDate',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='eventreport',
            name='endDate',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]