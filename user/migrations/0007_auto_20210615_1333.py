# Generated by Django 3.2.4 on 2021-06-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='reports',
            new_name='activityReports',
        ),
        migrations.AddField(
            model_name='user',
            name='eventReports',
            field=models.IntegerField(default=0),
        ),
    ]
