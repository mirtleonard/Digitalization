# Generated by Django 3.2.4 on 2021-06-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityReport', '0003_activityreport_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityreport',
            name='photo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]