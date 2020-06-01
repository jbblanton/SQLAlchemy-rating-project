"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Renders the homepage"""

    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """List of all movies"""

    movies = crud.create_movie_list()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    """Details on a chosen movie"""

    movie = crud.get_movie_details(movie_id)

    return render_template('movie_details.html', movie=movie)


@app.route('/all_users')
def all_users():
    """List of all users"""

    users = crud.create_user_list()

    return render_template('all_users.html', users=users)


@app.route('/all_users/<user_id>')
def user_details(user_id):
    """Details on a chosen user"""

    user = crud.get_user_details(user_id)

    return render_template('user_details.html', user=user)


@app.route('/users', methods=["POST"])
def add_user():
    """Check if email already has account; 
        create new user"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user == None:
        crud.create_user(email, password)
        flash('Account created! Please log in.')
    else:
        flash('Could not create an account with that email. Please try again!')

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
