
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','MovieAPI.settings')

import django 
django.setup()
from api.models import Movie
from api import *

from faker import Faker
from random import *

import random

faker=Faker() # creating faker object

def populate(n):
    genre=['Action','Thriller','Drama','Sci-fi']
    language=['English','German','Spanish']
    for i in range(n):
        fmname=faker.name()
        fmgenre=random.choice(genre)
        fmrelease=faker.year()
        fmlanguage=random.choice(language)
        movie_data=Movie.objects.get_or_create(name=fmname,genre=fmgenre,language=fmlanguage,release_year=fmrelease)

populate(250)  