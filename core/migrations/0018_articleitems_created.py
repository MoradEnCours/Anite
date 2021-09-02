# Generated by Django 3.0.12 on 2021-08-11 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_articleitems_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleitems',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]