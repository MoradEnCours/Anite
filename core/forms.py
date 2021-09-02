from django import forms
from django.forms.widgets import HiddenInput

REQUEST_CHOICES = (
    ('Anime', 'Anime'),
    ('Movie', 'Movie'),
    ('Others', 'Others'),
)


class RequestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Naruto Uzumaki'
    }))
    email_address = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'yourname@example.com'
    }))
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Your Name'
    }))
    season = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Season 1'
    }), required=False)
    choice = forms.ChoiceField(widget=forms.Select(), choices=REQUEST_CHOICES)
    message = forms.CharField(widget=forms.TextInput(attrs={
        "rows": 4,
        'placeholder': 'Have any message for us?'
    }), required=False)

#Moi

from core.models import ArticleItems, UserAccount

class ArticleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Enter title for article'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'col-md-12 form-it',
        'placeholder': 'Enter description for article'
    }))
    author = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-md-6 form-it',
        'placeholder': 'Your Name'
    }))


class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        # 'class': 'col-md-6 form-it',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        # 'class': 'col-md-6 form-it',
        'placeholder': 'yourname@example.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        # 'class': 'col-md-6 form-it',
        'placeholder': 'Your Password'
    }))
    image = forms.ImageField(required=False)




# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('picture',)


# '''
# Form for adding comments.
# '''
# class CommentForm(forms.ModelForm):
#     body = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control', 'rows': '1', 'cols': '10'}))
#     class Meta:
#         model = Comment
#         fields = ('body',)