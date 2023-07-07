from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from core.models import BaseModel,TimStampMixin
# Create your models here.

class User(AbstractUser):
    
    age = models.PositiveIntegerField(_("age"),blank=True,null=True)
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
    @property
    def followings_count(self) -> int:
        return self.followings.count()

    @property
    def followers_count(self) -> int:
        return self.followers.count()


    class Meta:
        verbose_name, verbose_name_plural = _("User"), _("Users")


class Relation(models.Model,TimStampMixin):
    from_user = models.ForeignKey("User",
                                    verbose_name=_("from_user"),
                                    on_delete=models.CASCADE,
                                    related_name="Following")
    to_user = models.ForeignKey("User",
                                    verbose_name=_("from_user"),
                                    on_delete=models.CASCADE,
                                    related_name="Followers")
  
    class Meta:
        verbose_name, verbose_name_plural = _("Relation"), _("Relations")

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
