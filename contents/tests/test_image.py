from django.test import TestCase
from models import Post, Image

class PostTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create()
        self.image_file = "path/to/image.jpg"  
        self.image_file1 = "path/to/image1.jpg"  
        self.image_file2 = "path/to/image2.jpg"  
        self.image = Image.objects.create(post=self.post)
        return super().setUp()

    def test_add_image(self):
        image = self.post.add_image(self.image_file)
        self.assertTrue(Image.objects.filter(id=image.id).exists())
        
    def test_remove_image(self):
        self.post.remove_image(self.image.id)
        self.assertFalse(Image.objects.filter(id=self.image.id).exists())
        
    def test_get_images(self):
        self.post.add_image(self.image_file1)
        self.post.add_image(self.image_file2)
        images = self.post.get_images()
        self.assertEqual(images.count(), 2)