from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Own user model, based on Django user model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='images/users',
        verbose_name="Image"
    )

    # deposit = models.ForeignKey(Deposit)

    def __unicode__(self):
        return self.user

    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
