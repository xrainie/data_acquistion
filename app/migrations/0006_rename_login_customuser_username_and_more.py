# Generated by Django 5.0.8 on 2024-08-06 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_customuser_date_joined'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='login',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
    ]
