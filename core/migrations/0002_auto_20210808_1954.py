# Generated by Django 3.0.12 on 2021-08-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default="{% static 'images/aniverse.png' %}", upload_to=''),
        ),
    ]