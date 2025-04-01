from django.test import TestCase
from Account.models import User, Token

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testing1", password_hash="hashing1", email="testing1@gmail.com")
        User.objects.create(username="testing2 ", password_hash="hashing2_", email="testing2_2@gmail.com")

    def test_basic_user_test(self):
        """Basic user creation is identified"""
        testing1 = User.objects.get(username="testing1")
        testing2 = User.objects.get(username="testing2")

        self.assertEqual(testing1.email, 'Email for first user is "testing1@gmail.com"')
        self.assertEqual(testing2.email, 'Email for second user is "testing2_2@gmail.com"')