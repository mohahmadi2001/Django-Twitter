from django.test import TestCase
from models import User, Relation

class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.user3 = User.objects.create(username='user3')
        Relation.objects.create(from_user=self.user1, to_user=self.user2)
        Relation.objects.create(from_user=self.user1, to_user=self.user3)

    def test_get_followers(self):
        followers = self.user1.get_followers()
        self.assertEqual(len(followers), 2)
        self.assertIn(self.user2, followers)
        self.assertIn(self.user3, followers)

    def test_follow(self):
        result1 = self.user1.follow(self.user2)
        result2 = self.user1.follow(self.user3)

        self.assertTrue(result1)
        self.assertTrue(result2)

        relation1 = Relation.objects.filter(from_user=self.user1, to_user=self.user2).exists()
        relation2 = Relation.objects.filter(from_user=self.user1, to_user=self.user3).exists()
        self.assertTrue(relation1)
        self.assertTrue(relation2)
        
        result = self.user1.follow(self.user1)

        self.assertFalse(result)

        relation = Relation.objects.filter(from_user=self.user1, to_user=self.user1).exists()
        self.assertFalse(relation)
        
    def test_unfollow(self):
        result1 = self.user1.unfollow(self.user2)
        result2 = self.user1.unfollow(self.user3)

        self.assertTrue(result1)
        self.assertTrue(result2)

        relation1 = Relation.objects.filter(from_user=self.user1, to_user=self.user2).exists()
        relation2 = Relation.objects.filter(from_user=self.user1, to_user=self.user3).exists()
        self.assertFalse(relation1)
        self.assertFalse(relation2)
        
        result = self.user1.unfollow(self.user3)

        self.assertFalse(result)

        relation = Relation.objects.filter(from_user=self.user1, to_user=self.user3).exists()
        self.assertFalse(relation)
