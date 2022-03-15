from django.db import models
from django.contrib.auth.models import User

class Blogger(models.Model):
    class Meta:
        ordering = ('user__username',)
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='User that is going to be an author'
    )
    
    bio = models.TextField(
        max_length=1000,
        help_text='Author\'s biography'
    )
    
    def __str__(self) -> str:
        return f'{self.user.username}'