from django.db import models
from django.utils.translation import gettext as _
from core.models import BaseModel,TimStampMixin
# Create your models here.

class User(BaseModel):
    username = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
        verbose_name=_("Username"),
        help_text="Username to login and show in the profile",
        blank=False,
        null=False)
    password = models.CharField(
        max_length=150,
        verbose_name=_("password"),
        help_text="password to login and show in the profile",
        blank=False,
        null=False)
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to='profilePhoto')
    bio = models.TextField(_("Biography"))
    
    def view_profile(self):
        profile = {
            'username': self.username,
            'image': self.image.url,
            'bio': self.bio,
        }
        return profile
    

class Relation(models.Model,TimStampMixin):
    from_user = models.ForeignKey("User",
                                    verbose_name=_("from_user"),
                                    on_delete=models.CASCADE,
                                    related_name="Following")
    to_user = models.ForeignKey("User",
                                    verbose_name=_("from_user"),
                                    on_delete=models.CASCADE,
                                    related_name="Followers")
  
    
    def get_followers(self):
        followers = Relation.objects.filter(to_user=self)
        return [follower.from_user for follower in followers]
    
    def follow(self, user):
        if user != self:
            relation, created = Relation.objects.get_or_create(from_user=self, to_user=user)
            if created:
                return True
        return False
    
    def unfollow(self, user):
        relation = Relation.objects.filter(from_user=self, to_user=user).first()
        if relation:
            relation.delete()
            return True
        return False

class Archive(models.Model):
    user_archive = models.ForeignKey("User",
                                     verbose_name=_("archive user"),
                                     on_delete=models.CASCADE)
    post_archive = models.ForeignKey("contents.Post",
                                     verbose_name=_("archive post"),
                                     on_delete=models.CASCADE)
    
    def archive_post(self, post):
        archive, created = Archive.objects.get_or_create(user_archive=self, post_archive=post)
        if created:
            return True
        return False
  
    
    def unarchive_post(self, post):
        archive = Archive.objects.filter(user_archive=self, post_archive=post).first()
        if archive:
            archive.delete()
            return True
        return False    