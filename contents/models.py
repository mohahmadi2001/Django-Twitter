from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel,TimStampMixin,SoftDeleteModel 
# Create your models here.

class Tag(BaseModel):
    text = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.text
    
    def add_tag(self, tag_text):
        tag, created = Tag.objects.get_or_create(text=tag_text)
        self.tags.add(tag)
        
    def remove_tag(self, tag_text):
        tag = Tag.objects.filter(text=tag_text).first()
        if tag:
            self.tags.remove(tag)
    
    def get_tags(self):
        return self.Tags.all()
    
    
class Post(TimStampMixin,SoftDeleteModel):
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        
    class Statuses(models.TextChoices):
        DRAFT = "D", _("Draft")
        PUBLISHED = "P", _("Published")
        
    text = models.TextField(verbose_name=_("Title"), help_text=_("Text to display"))
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    status = models.CharField(
        max_length=1,
        choices=Statuses.choices,
        default=Statuses.PUBLISHED,
    )
    tags = models.ManyToManyField(Tag, related_name="posts")

    
    
    def is_liked_by_user(self,user):
        return self.reaction_set.filter(user=user).exists()

    def archive(self):
        self.is_archived = True
        self.save()
        
    def unarchive(self):
        self.is_archived = False
        self.save()

   
class Image(BaseModel):
    image = models.FileField(_("Image"),
                             upload_to="post-images", 
                             max_length=100)
    related_post = models.ForeignKey("Post", 
                             verbose_name=_("post"),
                             on_delete=models.CASCADE,
                             related_name="image")
     
    def add_image(self, image_file):
        image = Image.objects.create(image=image_file, post=self)
        return image

    def remove_image(self, image_id):
        image = Image.objects.filter(id=image_id).first()
        if image:
            image.delete()
            
    def get_images(self):
        return self.image.all()
    

class Comment(BaseModel):
    text = models.TextField(_("text"))
    user = models.ForeignKey("account.User", 
                             verbose_name=_("user"),
                             on_delete=models.CASCADE)
    related_post = models.ForeignKey("Post", 
                             verbose_name=_("Post"),
                             on_delete=models.CASCADE)
    reply_to = models.ForeignKey("self", 
                                 verbose_name=_("comment"), 
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    
    def add_comment(self, user, text, reply_to=None):
        comment = Comment.objects.create(user=user, post=self, text=text, reply_to=reply_to)
        return comment
    
    def remove_comment(self, comment_id):
        comment = Comment.objects.filter(id=comment_id).first()
        if comment:
            comment.delete()
            
    def get_comments(self):
        return self.comment.all()
   
   
class Reaction(BaseModel):
    user = models.ForeignKey("account.User", 
                             verbose_name=_("user"),
                             on_delete=models.CASCADE)
    related_post = models.ForeignKey("Post", 
                             verbose_name=_("Post"),
                             on_delete=models.CASCADE)
    
    def like(self, user):
        reaction, created = Reaction.objects.get_or_create(user=user, post=self)
        if created:
            return True
        return False
    
    def unlike(self, user):
        reaction = Reaction.objects.filter(user=user, post=self).first()
        if reaction:
            reaction.delete()
            return True
        return False