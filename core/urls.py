from django.urls import path
from .views import (IndexView,
                    ItemDetailView,
                    AnimeListingView, LandingDetailView, RegisterAccount,
                    Search,
                    AnimeGridingView,
                    MovieDetailView,
                    MovieGridingView,
                    RequestView,
                    CharacterDetailView,
                    ComingSoonView,
                    ErrorView,
                    BlogListView,
                    BlogDetailView,
                    CreateArticle,
                    RegisterAccount,
                    ProfileDetailView,
                    LandingDetailView,
                    )

from django.views.generic import TemplateView


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('anime/<pk>/', ItemDetailView.as_view(), name="anime"),
    path('movie/<pk>/', MovieDetailView.as_view(), name="movie"),
    path('anime_all/list/', AnimeListingView.as_view(), name="anime-listing"),
    path('anime_all/grid/', AnimeGridingView.as_view(), name="anime-griding"),
    path('movie_all/grid/', MovieGridingView.as_view(), name="movie-griding"),
    path('search/anime/', Search.as_view(), name="search"),
    path('request-us/', RequestView.as_view(), name="request-us"),
    path('characters/<slug>/', CharacterDetailView.as_view(),
         name="character-details"),
    path('coming-soon/', ComingSoonView.as_view(), name="coming-soon"),
    path('404/', ErrorView.as_view()),
    path('bloglist/', BlogListView.as_view()),
    path('bloglist/<slug>', BlogDetailView.as_view(), name="blog-details"),
    path('blogdetail/', BlogDetailView.as_view()),
    path('bloglist/create-article/',
         CreateArticle.as_view(), name="create-article"),
    path('register/', RegisterAccount.as_view()),
    path('profile/<slug>', ProfileDetailView.as_view()),
    path('landing/', LandingDetailView.as_view(), name="landing"),

]
