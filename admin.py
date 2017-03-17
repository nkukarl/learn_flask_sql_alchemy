from sqlalchemy.exc import IntegrityError
from main import db
from user import User

class Admin(object):
    def __init__(self, username, password):
        if (username, password) != ('kwang', '123'):
            raise PermissionError('Incorrect username, password combination!')

    def add_users(self, usernames, emails):
        """

        :param usernames (list):
        :param emails (list):

        """
        for username, email in zip(usernames, emails):
            user = User(username, email)
            db.session.add(user)
        db.session.commit()

    def list_users(self):
        """

        :return:
            A list of users

        """
        return User.query.all()

    def get_user_by_username(self, username):
        """

        :param username (str):
        :return:
            A User object whose username matches username provided
        """

        return User.query.filter_by(username=username).first()
