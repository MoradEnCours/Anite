# Generated by Django 3.0.12 on 2021-08-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210809_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleitems',
            name='author',
            field=models.CharField(default='moi', max_length=50),
        ),
        migrations.AddField(
            model_name='articleitems',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
