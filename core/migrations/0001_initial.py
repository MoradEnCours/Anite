# Generated by Django 3.0.12 on 2021-08-07 22:07

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Anime Categories',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('role', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.')),
                ('detailed_description', ckeditor_uploader.fields.RichTextUploadingField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.')),
                ('date_of_birth', models.DateField()),
                ('height', models.FloatField()),
                ('slug', models.SlugField()),
                ('father_character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father', to='core.Character')),
                ('mother_character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother', to='core.Character')),
            ],
            options={
                'verbose_name_plural': 'Characters',
            },
        ),
        migrations.CreateModel(
            name='CharacterSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('characters', models.ManyToManyField(blank=True, to='core.Character')),
            ],
            options={
                'verbose_name_plural': 'CharacterSets',
            },
        ),
        migrations.CreateModel(
            name='InsightDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('production_house', models.CharField(max_length=50)),
                ('writers', models.CharField(max_length=50)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('total_episodes', models.IntegerField(default=25)),
                ('season_number', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Insight Details',
            },
        ),
        migrations.CreateModel(
            name='MediaAttachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('is_video', models.BooleanField()),
                ('video_url', models.URLField(blank=True, null=True)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('characters', models.ManyToManyField(blank=True, to='core.Character')),
            ],
            options={
                'verbose_name_plural': 'Media Attachments',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('season', models.CharField(blank=True, max_length=100, null=True)),
                ('choice', models.CharField(max_length=40)),
                ('request_accepted', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Requested Animes/Movies',
            },
        ),
        migrations.CreateModel(
            name='VideoItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('runtime', models.CharField(max_length=9)),
                ('publish', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Videos, AMV, Trailers',
            },
        ),
        migrations.CreateModel(
            name='MovieItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_english', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.')),
                ('rating', models.FloatField(default=7.0)),
                ('votes', models.IntegerField(default=1000)),
                ('editors_pick', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Slice of Life', 'Slice of Life'), ('Fantasy', 'Fantasy'), ('Magic', 'Magic'), ('Supernatural', 'Supernatural'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Psychological', 'Psychological'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi')], max_length=114)),
                ('year_released', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2017)),
                ('language', models.CharField(choices=[('Dual Audio', 'Dual Audio'), ('Subbed', 'Subbed'), ('Dubbed', 'Dubbed')], default='Subbed', max_length=30)),
                ('character_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.CharacterSet')),
                ('insights', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.InsightDetails')),
                ('media', models.ManyToManyField(blank=True, to='core.MediaAttachments')),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_english', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.')),
                ('rating', models.FloatField(default=7.0)),
                ('votes', models.IntegerField(default=1000)),
                ('ongoing', models.BooleanField(default=True)),
                ('editors_pick', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('genres', multiselectfield.db.fields.MultiSelectField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Slice of Life', 'Slice of Life'), ('Fantasy', 'Fantasy'), ('Magic', 'Magic'), ('Supernatural', 'Supernatural'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Psychological', 'Psychological'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi')], max_length=114)),
                ('sub_genres', multiselectfield.db.fields.MultiSelectField(choices=[('Cyberpunk', 'Cyberpunk'), ('Game', 'Game'), ('Ecchi', 'Ecchi'), ('Demons', 'Demons'), ('Harem', 'Harem'), ('Josei', 'Josei'), ('Martial Arts', 'Martial Arts'), ('Kids', 'Kids'), ('Historical', 'Historical'), ('Hentai', 'Hentai'), ('Isekai', 'Isekai'), ('Military', 'Military'), ('Mecha', 'Mecha'), ('Music', 'Music'), ('Parody', 'Parody'), ('Police', 'Police'), ('Post-Apocalyptic', 'Post-Apocalyptic'), ('Reverse Harem', 'Reverse Harem'), ('School', 'School'), ('Seinen', 'Seinen'), ('Shoujo', 'Shoujo'), ('Shoujo-ai', 'Shoujo-ai'), ('Shounen', 'Shounen'), ('Shounen-ai', 'Shounen-ai'), ('Space', 'Space'), ('Sports', 'Sports'), ('Super Power', 'Super Power'), ('Tragedy', 'Tragedy'), ('Vampire', 'Vampire'), ('Yuri', 'Yuri'), ('Yaoi', 'Yaoi')], max_length=249)),
                ('year_released', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2017)),
                ('language', models.CharField(choices=[('Dual Audio', 'Dual Audio'), ('Subbed', 'Subbed'), ('Dubbed', 'Dubbed')], default='Subbed', max_length=30)),
                ('character_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.CharacterSet')),
                ('insights', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.InsightDetails')),
                ('media', models.ManyToManyField(blank=True, to='core.MediaAttachments')),
            ],
            options={
                'verbose_name': 'Anime',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='part_of_animes',
            field=models.ManyToManyField(blank=True, related_name='animes_related', to='core.Item'),
        ),
        migrations.AddField(
            model_name='character',
            name='part_of_movies',
            field=models.ManyToManyField(blank=True, related_name='movies_related', to='core.MovieItem'),
        ),
        migrations.AddField(
            model_name='character',
            name='spouse_character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spouse', to='core.Character'),
        ),
    ]
