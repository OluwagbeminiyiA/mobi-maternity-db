# Generated by Django 5.1 on 2024-08-22 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userregistration_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
