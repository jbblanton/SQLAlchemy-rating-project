"""Automate the creation of a database, Seed the info"""

import os
import json
from random import choice, randint
from datetime import datetime
import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

#Open and access the movie data via JSON file
with open('data/movies.json') as f: 
    movie_data = json.loads(f.read())

#Create movie objects; Store in a list
movies_in_db = []

for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    release_date = datetime.strptime(movie['release_date'], "%Y-%m-%d")

    mov = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(mov) 

for n in range(10):
    email = f'user{n}@aol.com'
    password = 'test123'

    user = crud.create_user(email, password)

    for num in range(10):
        movie = choice(movies_in_db)
        score = randint(1, 5)

        crud.create_rating(user, movie, score)
