from django.test import TestCase
from models import Post, Comment
from account.models import User

class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create()
        self.user = User.objects.create(username="testuser")
        self.comment = Comment.objects.create(user=self.user, post=self.post, text="Test Comment")
        self.comment1 = Comment.objects.create(user=self.user, post=self.post, text="Test Comment 1")
        return super().setUp()

    def test_add_comment(self):
        text = "This is a test comment."
        comment = self.post.add_comment(user=self.user, text=text)
        self.assertEqual(comment.text, text)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertIsNone(comment.reply_to)
        
    def test_remove_comment(self):
        comment_id = self.comment.id
        self.post.remove_comment(comment_id)
        comment = Comment.objects.filter(id=comment_id).first()
        self.assertIsNone(comment)
        
    def test_get_comments(self):
        comments = self.post.get_comments()
        self.assertEqual(comments.count(), 2)
        self.assertIn(self.comment, comments)
        self.assertIn(self.comment1, comments)