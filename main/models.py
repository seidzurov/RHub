from django.db import models

from users.models import Profile


class Publications(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True)
    likes = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.username
    
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'