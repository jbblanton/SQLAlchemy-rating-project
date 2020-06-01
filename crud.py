"""Automating the CRUD"""

from model import db, User, Movie, Rating, connect_to_db

def create_user(email, password):
    """Create & return new user"""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_user_list():
    """Create a list of all users,
        for display on '/users' """

    return User.query.all()


def get_user_details(user_id):
    """Get the details on a chosen user"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Check if user already exists in the database"""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create a new movie entry"""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def create_movie_list():
    """Create a list of movie titles, 
        for display on '/movies' """

    return Movie.query.all()


def get_movie_details(movie_id):
    """Get the details of a chosen movie"""

    return Movie.query.get(movie_id)


def create_rating(user, movie, score):
    """Let a user rate a movie"""

    rating = Rating(score=score, user=user, movie=movie)


    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)