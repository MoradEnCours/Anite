# Generated by Django 3.0.12 on 2021-08-11 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210809_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleitems',
            old_name='title',
            new_name='name',
        ),
    ]