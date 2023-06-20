from django.test import TestCase
from models import User

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', image='test.jpg', bio='Test bio')

    def test_view_profile(self):
        profile = self.user.view_profile()
        self.assertEqual(profile['username'], 'testuser')
        self.assertEqual(profile['image'], 'test.jpg')
        self.assertEqual(profile['bio'], 'Test bio')
