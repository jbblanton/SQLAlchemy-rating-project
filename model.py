"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True, 
                        nullable = False,)
    email = db.Column(db.String(50), unique = True, nullable = False,)
    password = db.Column(db.String(20), nullable = False,)

    def __repr__(self):
        return f'<User user_id={self.user_id}, email={self.email}>'


class Movie(db.Model):
    """A movie"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key = True, 
                        autoincrement = True,)
    title = db.Column(db.String(), nullable = False,)
    overview = db.Column(db.Text,)
    release_date = db.Column(db.DateTime(), nullable = False,)
    poster_path = db.Column(db.String(100),)

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id}, title={self.title}, \
                 release={self.release_date}>'


class Rating(db.Model):
    """A rating"""

    rating_id = db.Column(db.Integer, primary_key = True, autoincrement = True,)
    score = db.Column(db.Integer, nullable = False)
    movie_id = db.Column(db.Integer, foreign_key('movies.movie_id'))
    user_id = db.Column(db.Integer, foreign_key('users.user_id'))

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id}, score={self.score}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
