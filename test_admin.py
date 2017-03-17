import time
from unittest import TestCase

from admin import Admin
from main import db
from user import User


class TestAdmin(TestCase):

    admin = Admin(username='kwang', password='123')

    def _prepare_user_info(self):
        time.sleep(1)
        time_stamp = str(int(time.time()))
        username = 'guest' + time_stamp
        email = username + '@kwang.com'
        return username, email

    def test_add_users(self):
        # Setup
        username, email = self._prepare_user_info()

        # Exercise
        self.admin.add_users([username], [email])

        # Verify
        users = User.query.all()
        usernames = [user.username for user in users]
        emails = [user.email for user in users]
        self.assertIn(username, usernames)
        self.assertIn(email, emails)

    def test_list_users(self):
        # Setup
        username, email = self._prepare_user_info()
        db.session.add(User(username, email))
        db.session.commit()

        # Exercise
        users = self.admin.list_users()

        # Verify
        usernames = [user.username for user in users]
        emails = [user.email for user in users]
        self.assertIn(username, usernames)
        self.assertIn(email, emails)

    def test_get_user_by_username(self):
        # Setup
        username, email = self._prepare_user_info()
        db.session.add(User(username, email))
        db.session.commit()

        # Exercise
        user = self.admin.get_user_by_username(username)

        # Verify
        self.assertEqual(username, user.username)
        self.assertEqual(email, user.email)
