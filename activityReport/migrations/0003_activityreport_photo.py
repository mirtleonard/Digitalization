# Generated by Django 3.2.4 on 2021-06-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityReport', '0002_auto_20210616_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityreport',
            name='photo',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]