from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('blog:blogger-detail', args=(self.id,))
    
    def get_last_blog(self):
        return self.blog_set.latest('post_date')