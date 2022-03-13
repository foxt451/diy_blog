from django.db import models
from .blog import Blog
from django.contrib.auth.models import User


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        help_text='Blog being commented'
    )
    
    commenter = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        help_text='The person commenting on the blog'
    )
    
    content = models.TextField(
        max_length=1000,
        help_text='Text of the comment'
    )
    
    post_date = models.DateTimeField(
        'Posted',
        auto_now_add=True,
        help_text='Time when comment was posted'
    )