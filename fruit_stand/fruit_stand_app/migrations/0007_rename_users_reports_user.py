# Generated by Django 5.1.1 on 2024-09-19 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_stand_app', '0006_reports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reports',
            old_name='users',
            new_name='user',
        ),
    ]
