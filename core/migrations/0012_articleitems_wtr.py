# Generated by Django 3.0.12 on 2021-08-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210809_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleitems',
            name='wtr',
            field=models.URLField(default='http://127.0.0.1:8000/'),
        ),
    ]
