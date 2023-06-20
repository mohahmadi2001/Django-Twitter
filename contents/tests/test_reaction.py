from django.test import TestCase
from models import Post
from account.models import User

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create()

    def test_like(self):
        self.assertFalse(self.post.is_liked_by_user(self.user))

        self.post.like(self.user)

        self.assertTrue(self.post.is_liked_by_user(self.user))

        self.post.like(self.user)

        self.assertTrue(self.post.is_liked_by_user(self.user))

        self.post.unlike(self.user)

        self.assertFalse(self.post.is_liked_by_user(self.user))

    def test_unlike(self):
        self.assertFalse(self.post.is_liked_by_user(self.user))

        self.post.like(self.user)

        self.assertTrue(self.post.is_liked_by_user(self.user))

        self.post.unlike(self.user)

        self.assertFalse(self.post.is_liked_by_user(self.user))

        self.post.unlike(self.user)

        self.assertFalse(self.post.is_liked_by_user(self.user))