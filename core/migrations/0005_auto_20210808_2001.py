# Generated by Django 3.0.12 on 2021-08-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210808_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='static/aniverse.png', upload_to=''),
        ),
    ]
