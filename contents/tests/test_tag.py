from django.test import TestCase
from models import Tag,Post

class TagTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create()
        self.tag1 = Tag.objects.create(text="Tag1")
        self.tag2 = Tag.objects.create(text="Tag2")
        self.post.tags.add(self.tag1, self.tag2)
        return super().setUp()
    
    def test_add_tag(self):
        tag_text = "example tag"
        self.post.add_tag(tag_text)

        self.assertEqual(self.post.tags.count(), 1)
        
        tag = self.post.tags.first()
        self.assertEqual(tag.text, tag_text)
    
    def test_remove_tag(self):
        self.post.remove_tag("Tag1")
        self.assertEqual(self.post.tags.count(), 1)
        self.assertFalse(self.tag1 in self.post.tags.all())
        
        self.post.remove_tag("Tag3")
        self.assertEqual(self.post.tags.count(), 2)
        
        self.post.tags.add(self.tag1)
        self.post.remove_tag("Tag1")
        self.assertEqual(self.post.tags.count(), 1)
        self.assertFalse(self.tag1 in self.post.tags.all())
        
        empty_post = Post.objects.create()
        empty_post.remove_tag("Tag1")
        self.assertEqual(empty_post.tags.count(), 0)
        
    def test_get_tag(self):
        tags = self.post.get_tags()
        self.assertEqual(len(tags), 2)
        self.assertTrue(self.tag1 in tags)
        self.assertTrue(self.tag2 in tags)
        
        empty_post = Post.objects.create()
        tags = empty_post.get_tags()
        self.assertEqual(len(tags), 0)