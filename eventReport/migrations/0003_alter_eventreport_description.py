# Generated by Django 3.2.4 on 2021-07-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventReport', '0002_auto_20210616_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventreport',
            name='description',
            field=models.TextField(),
        ),
    ]