from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self', 
        related_name="followers", 
        symmetrical=False,
        blank=True
    )
    nickname = models.CharField(max_length=255, default=str("User"))
    bio = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(blank=True, null=True)


    def __str__(self):
        return f"{self.nickname}({self.user.username})"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
