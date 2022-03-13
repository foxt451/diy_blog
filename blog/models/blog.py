from django.db import models
from .blogger import Blogger

class Blog(models.Model):
    post_date = models.DateTimeField(
        'Posted',
        auto_now_add=True,
        help_text='The time when the blog is created'
    )
    
    author = models.ForeignKey(
        Blogger,
        on_delete=models.SET_NULL,
        null=True,
        help_text='Author of the blog'
    )
    
    title = models.CharField(max_length=100, help_text='Blog\'s title')
    content = models.TextField(max_length=10_000, help_text='Blog\'s content')
    