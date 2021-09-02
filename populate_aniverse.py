import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aniverse.settings')

import django
django.setup()
from core.models import Item, MovieItem, VideoItems, Request, Character



def populate():

    mitem = [
        {
            "title" : "1",
            "image" : "pexels-photo-152536.jpeg",
            "background_image" : "pexels-photo-152536.jpeg",
            "description" : "4",
            "rating" : 5.5,
            "genres" : "Action",
            "sub_genres" : "Game",            
        }
    ]

    # def add_movie('title', 'title_english', 'image', 'background_image', 'description', 'rating', 'votes', 'editors_pick', 'created', 'updated', 'genres', 'year_released', 'media', 'insights', 'character_set', 'language'):

        

    def add_request(title,image,background_image,description,rating,genres):
        request = MovieItem.objects.get_or_create(title="1",image="pexels-photo-152536.jpeg",background_image="pexels-photo-152536.jpeg",description="4",rating=5.5,genres="Action")[0]
        request.save()
        return request

    add_request(1,2,3,4,5,6)

if __name__ == '__main__':
    print('Running the lanex population script...   [Random Fun fact - Wearing headphones for just an hour can raise  bacteria count in the ears by 700 times] ')
    populate()