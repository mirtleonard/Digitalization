# Generated by Django 3.2.4 on 2021-06-11 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_eventreport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Report',
            new_name='ActivityReport',
        ),
    ]
