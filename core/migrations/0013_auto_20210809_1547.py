# Generated by Django 3.0.12 on 2021-08-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_articleitems_wtr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleitems',
            options={'verbose_name_plural': 'ArticleItems'},
        ),
        migrations.AddField(
            model_name='articleitems',
            name='url',
            field=models.SlugField(default='blogdetail'),
        ),
    ]