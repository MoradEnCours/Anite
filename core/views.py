from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, View
from .models import Item, MovieItem, UserAccount, VideoItems, Request, Character
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from .forms import RequestForm
from django.contrib import messages

# Moi
from django.views.generic import TemplateView
from .models import ArticleItems, UserAccount
from .forms import ArticleForm, RegistrationForm

def latest_updated_list():
    return Item.objects.order_by("-created")[:20]

#Moi
def arlatest_updated_list():
    return ArticleItems.objects.order_by("-created")[:20]


def testing(request):
    return render(request, 'request-anime.html')


class Search(ListView):
    def get(self, *args, **kwargs):
        # url/?q="_____"
        # will be our search query
        queryset = Item.objects.all()
        movieset = MovieItem.objects.all()
        characterset = Character.objects.all()
        query = self.request.GET.get('search_item')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(title_english__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
            movieset = movieset.filter(
                Q(title__icontains=query) |
                Q(title_english__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
            characterset = characterset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        result_list = list(chain(queryset, movieset, characterset))
        context = {
            'results': result_list,
            'query': query
        }
        return render(self.request, 'search-grid.html', context)


class AnimeListingView(View):
    def get(self, *args, **kwargs):
        queryset = Item.objects.all()

        paginator = Paginator(queryset, 10)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'listing.html', context)


class AnimeGridingView(View):
    def get(self, *args, **kwargs):
        queryset = Item.objects.all()

        paginator = Paginator(queryset, 30)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'griding.html', context)


class MovieGridingView(View):
    def get(self, *args, **kwargs):
        queryset = MovieItem.objects.all()

        paginator = Paginator(queryset, 30)
        page_requested_var = 'page'
        page = self.request.GET.get(page_requested_var)
        try:
            paginated_queryset = paginator.page(page)
        except PageNotAnInteger:
            paginated_queryset = paginator.page(1)
        except EmptyPage:
            paginated_queryset = paginator.page(paginator.num_pages)
        context = {
            'object_list': queryset,
            'page_number': page_requested_var,
            'queryset': paginated_queryset
        }
        return render(self.request, 'movielisting-grid.html', context)


class IndexView(View):
    def get(self, *args, **kwargs):
        latest_updated = latest_updated_list()
        ongoing_list = Item.objects.filter(ongoing=True).order_by("-updated")
        rated_list = Item.objects.filter(ongoing=True).order_by("-rating")
        voted_list = Item.objects.filter(ongoing=True).order_by("-votes")
        editor_list = Item.objects.filter(ongoing=True, editors_pick=True)

        rated_movie_list = MovieItem.objects.order_by("-rating")
        latest_movie_list = MovieItem.objects.order_by("-created")

        videos = VideoItems.objects.filter(publish=True).order_by("-created_at")
        context = {
            'latest_list': latest_updated,
            'ongoing_list': ongoing_list,
            'rated_list': rated_list,
            'voted_list': voted_list,
            'editor_list': editor_list,
            'latest_movie_list': latest_movie_list,
            'rated_movie_list': rated_movie_list,
            'videos': videos,
        }
        return render(self.request, "index.html", context)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'anime-single.html'


class MovieDetailView(DetailView):
    model = MovieItem
    template_name = 'movie-single.html'


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character-details.html'


class RequestView(View):
    def get(self, *args, **kwargs):
        form = RequestForm()
        context = {
            'form': form
        }
        return render(self.request, 'request-anime.html', context)

    def post(self, *args, **kwargs):
        form = RequestForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email_address = form.cleaned_data.get('email_address')
            title = form.cleaned_data.get('title')
            season = form.cleaned_data.get('season')
            choice = form.cleaned_data.get('choice')
            message = form.cleaned_data.get('message')
            try:
                request = Request()
                request.name = name
                request.email_address = email_address
                request.title = title
                request.season = season
                request.choice = choice
                request.message = message
                request.save()
                messages.success(self.request, "We have successfully received your request. Thank You!")
                return redirect("core:index")
            except:
                messages.info(self.request, "Something went wrong! Please retry after some time.")
                return redirect("core:request-us")
        else:
            messages.info(self.request, "Something went wrong! Please retry after some time.")
            return redirect("core:request-us")


#Moi

class ComingSoonView(View):
     def get(self, *args, **kwargs):
        latest_updated = latest_updated_list()
        ongoing_list = Item.objects.filter(ongoing=True).order_by("-updated")
        rated_list = Item.objects.filter(ongoing=True).order_by("-rating")
        voted_list = Item.objects.filter(ongoing=True).order_by("-votes")
        editor_list = Item.objects.filter(ongoing=True, editors_pick=True)

        rated_movie_list = MovieItem.objects.order_by("-rating")
        latest_movie_list = MovieItem.objects.order_by("-created")

        videos = VideoItems.objects.filter(publish=True).order_by("-created_at")
        context = {
            'latest_list': latest_updated,
            'ongoing_list': ongoing_list,
            'rated_list': rated_list,
            'voted_list': voted_list,
            'editor_list': editor_list,
            'latest_movie_list': latest_movie_list,
            'rated_movie_list': rated_movie_list,
            'videos': videos,
        }
        return render(self.request, "comingsoon.html", context)

class ErrorView(TemplateView):
    template_name = "404.html"

class BlogListView(View):
    # template_name = "bloglist.html"
     def get(self, *args, **kwargs):
        latest_updated = latest_updated_list()
        ar_latest_updated = arlatest_updated_list()
        ongoing_list = Item.objects.filter(ongoing=True).order_by("-updated")
        rated_list = Item.objects.filter(ongoing=True).order_by("-rating")
        voted_list = Item.objects.filter(ongoing=True).order_by("-votes")
        editor_list = Item.objects.filter(ongoing=True, editors_pick=True)

        rated_movie_list = MovieItem.objects.order_by("-rating")
        latest_movie_list = MovieItem.objects.order_by("-created")

        videos = VideoItems.objects.filter(publish=True).order_by("-created_at")

        form = RequestForm()

        context = {
            'arlatest_list' : ar_latest_updated,
            'latest_list': latest_updated,
            'ongoing_list': ongoing_list,
            'rated_list': rated_list,
            'voted_list': voted_list,
            'editor_list': editor_list,
            'latest_movie_list': latest_movie_list,
            'rated_movie_list': rated_movie_list,
            'videos': videos,
            'form': form
        }
        return render(self.request, "bloglist.html", context)
        
    # def get(self, *args, **kwargs):
    #     form = RequestForm()
    #     context = {
    #         'form': form
    #     }
    #     return render(self.request, 'bloglist.html', context)


class CreateArticle(View):
    def get(self, *args, **kwargs):
        form2 = ArticleForm()
        context = {
            'form2' : form2
        }
        return render(self.request, 'create-article.html', context)

    def post(self, *args, **kwargs):
        form2 = ArticleForm(self.request.POST)
        if form2.is_valid():
            name = form2.cleaned_data.get('name')
            description = form2.cleaned_data.get('description')
            author = form2.cleaned_data.get('author')
            try:
                article = ArticleItems()
                article.name = name
                article.description = description
                article.author = author
                article.save()
                messages.success(self.request, "We have successfully received your request. Thank You!")
                return redirect("core:create-article")
            except:
                messages.info(self.request, "Something went wrong! Please retry after some time.")
                return redirect("core:request-us")
        else:
            messages.info(self.request, "Something went wrong! Please retry after some time.")
            return redirect("core:create-article")
            
    
class BlogDetailView(DetailView):
    model = ArticleItems
    template_name = "blogdetail.html"


class RegisterAccount(View):
    def get(self, *args, **kwargs):
        form = RegistrationForm()
        context = {
            'form' : form
        }
        return render(self.request, 'register.html', context)

    def post(self, *args, **kwargs):
        form = RegistrationForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                article = UserAccount()
                article.name = name
                article.email = email
                article.password = password
                article.save()
                messages.success(self.request, "We have successfully created your account. Thank You!")
                return redirect("core:index")
            except:
                messages.info(self.request, "Something went wrong! Please retry after some time.")
                return redirect("core:request-us")
        else:
            messages.info(self.request, "Something went wrong! Please retry after some time.")
            return redirect("core:create-article")


class ProfileDetailView(DetailView):
    model = UserAccount
    template_name = 'userprofile.html'


class LandingDetailView(TemplateView):
    template_name = 'landing.html'