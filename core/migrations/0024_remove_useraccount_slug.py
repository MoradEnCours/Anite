# Generated by Django 3.0.12 on 2021-08-23 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_useraccount_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='slug',
        ),
    ]
