from typing import Optional
from django.db import models
from django.shortcuts import reverse
from multiselectfield import MultiSelectField
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from itertools import chain

AUDIO_CHOICES = (
    ('Dual Audio', 'Dual Audio'),
    ('Subbed', 'Subbed'),
    ('Dubbed', 'Dubbed'),
)

GENRES_CHOICES = (
    ('Action', 'Action'),
    ('Adventure', 'Adventure'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Slice of Life', 'Slice of Life'),
    ('Fantasy', 'Fantasy'),
    ('Magic', 'Magic'),
    ('Supernatural', 'Supernatural'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Psychological', 'Psychological'),
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi')
)

SUB_GENRES_CHOICES = (
    ('Cyberpunk', 'Cyberpunk'),
    ('Game', 'Game'),
    ('Ecchi', 'Ecchi'),
    ('Demons', 'Demons'),
    ('Harem', 'Harem'),
    ('Josei', 'Josei'),
    ('Martial Arts', 'Martial Arts'),
    ('Kids', 'Kids'),
    ('Historical', 'Historical'),
    ('Hentai', 'Hentai'),
    ('Isekai', 'Isekai'),
    ('Military', 'Military'),
    ('Mecha', 'Mecha'),
    ('Music', 'Music'),
    ('Parody', 'Parody'),
    ('Police', 'Police'),
    ('Post-Apocalyptic', 'Post-Apocalyptic'),
    ('Reverse Harem', 'Reverse Harem'),
    ('School', 'School'),
    ('Seinen', 'Seinen'),
    ('Shoujo', 'Shoujo'),
    ('Shoujo-ai', 'Shoujo-ai'),
    ('Shounen', 'Shounen'),
    ('Shounen-ai', 'Shounen-ai'),
    ('Space', 'Space'),
    ('Sports', 'Sports'),
    ('Super Power', 'Super Power'),
    ('Tragedy', 'Tragedy'),
    ('Vampire', 'Vampire'),
    ('Yuri', 'Yuri'),
    ('Yaoi', 'Yaoi')
)

DEFAULT_DESCRIPTION = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class MediaAttachments(models.Model):
    image = models.ImageField()
    is_video = models.BooleanField()
    video_url = models.URLField(blank=True, null=True)
    added_date = models.DateTimeField(auto_now=True)
    characters = models.ManyToManyField('Character', blank=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Media Attachments"


class AnimeCategory(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Anime Categories"


class InsightDetails(models.Model):
    title = models.CharField(max_length=100)
    production_house = models.CharField(max_length=50)
    writers = models.CharField(max_length=50)
    director = models.CharField(max_length=50, blank=True, null=True)
    total_episodes = models.IntegerField(default=25)
    season_number = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Insight Details"


class Character(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    background_image = models.ImageField(blank=True, null=True)
    role = models.CharField(max_length=50, default='')
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    detailed_description = RichTextUploadingField(default=DEFAULT_DESCRIPTION)
    date_of_birth = models.DateField()
    height = models.FloatField()
    spouse_character = models.ForeignKey('self', related_name='spouse', on_delete=models.SET_NULL, blank=True,
                                         null=True)
    father_character = models.ForeignKey('self', related_name='father', on_delete=models.SET_NULL, blank=True,
                                         null=True)
    mother_character = models.ForeignKey('self', related_name='mother', on_delete=models.SET_NULL, blank=True,
                                         null=True)
    part_of_animes = models.ManyToManyField('Item', related_name="animes_related", blank=True)
    part_of_movies = models.ManyToManyField('MovieItem', related_name="movies_related", blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:character-details", kwargs={
            'slug': self.slug
        })

    def get_part_of(self):
        return list(chain(self.part_of_animes.all(), self.part_of_movies.all()))

    class Meta:
        verbose_name_plural = 'Characters'


class CharacterSet(models.Model):
    title = models.CharField(max_length=100)
    characters = models.ManyToManyField(Character, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "CharacterSets"


class Item(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default="aniverse.png")
    background_image = models.ImageField(blank=True, null=True)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    rating = models.FloatField(default=7.0)
    votes = models.IntegerField(default=1000)
    ongoing = models.BooleanField(default=True)
    editors_pick = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    genres = MultiSelectField(choices=GENRES_CHOICES)
    sub_genres = MultiSelectField(choices=SUB_GENRES_CHOICES)
    year_released = models.IntegerField(choices=year_choices(), default=current_year() - 4)
    media = models.ManyToManyField(MediaAttachments, blank=True)
    insights = models.ForeignKey(InsightDetails, blank=True, on_delete=models.CASCADE)
    character_set = models.ForeignKey(CharacterSet, blank=True, null=True, on_delete=models.SET_NULL)
    language = models.CharField(choices=AUDIO_CHOICES, max_length=30, default='Subbed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Anime'

    def get_absolute_url(self):
        return reverse("core:anime", kwargs={
            'pk': self.id
        })

    def media_qs(self):
        return self.media.order_by('-added_date')[:4]

    def get_image_count(self):
        return self.media.filter(is_video=False).count()

    def get_video_count(self):
        return self.media.filter(is_video=True).count()


class MovieItem(models.Model):
    title = models.CharField(max_length=100)
    title_english = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default=None)
    background_image = models.ImageField(blank=True, null=True)
    description = models.TextField(default=DEFAULT_DESCRIPTION)
    rating = models.FloatField(default=7.0)
    votes = models.IntegerField(default=1000)
    editors_pick = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    genres = MultiSelectField(choices=GENRES_CHOICES)
    year_released = models.IntegerField(choices=year_choices(), default=current_year() - 4)
    media = models.ManyToManyField(MediaAttachments, blank=True)
    insights = models.ForeignKey(InsightDetails, blank=True, on_delete=models.CASCADE)
    character_set = models.ForeignKey(CharacterSet, blank=True, null=True, on_delete=models.SET_NULL)
    language = models.CharField(choices=AUDIO_CHOICES, max_length=30, default='Subbed')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Movies'

    def get_absolute_url(self):
        return reverse("core:movie", kwargs={
            'pk': self.id
        })

    def media_qs(self):
        return self.media.order_by('-added_date')[:4]

    def get_image_count(self):
        return self.media.filter(is_video=False).count()

    def get_video_count(self):
        return self.media.filter(is_video=True).count()


class VideoItems(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    url = models.URLField()
    runtime = models.CharField(max_length=9)
    publish = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Videos, AMV, Trailers"

    def __str__(self):
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    title = models.CharField(max_length=100)
    season = models.CharField(max_length=100, blank=True, null=True)
    choice = models.CharField(max_length=40)
    request_accepted = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Requested Animes/Movies"


#Moi
from django.template.defaultfilters import slugify


class ArticleItems(models.Model):
    name = models.CharField(max_length=40, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    image = models.ImageField(default="aniverse.png")
    author = models.CharField(max_length=50, default="moi")
    views = models.IntegerField(default=0)
    wtr = models.URLField(default='http://127.0.0.1:8000/')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ArticleItems"

    def get_absolute_url(self):
        return reverse("core:blogdetail", kwargs={
            'slug': self.slug
        })
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArticleItems, self).save(*args, **kwargs)


class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="Last Name")
    country = models.CharField(max_length=100, default="Country")
    city = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    image = models.ImageField(default="aniverse.png")
    slug = models.SlugField(default="example")
    #url = models.URLField()
    #runtime = models.CharField(max_length=9)
    #publish = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "UserAccounts"

    def get_absolute_url(self):
        return reverse("core:userprofile", kwargs={
            'slug': self.slug
        })
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(UserAccount, self).save(*args, **kwargs)

    def __str__(self):
        return self.name