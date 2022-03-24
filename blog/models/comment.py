from django.db import models
from .blog import Blog
from django.template.defaultfilters import truncatechars
from django.conf import settings


class Comment(models.Model):
    class Meta:
        ordering = ('post_date',)
    
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        help_text='Blog being commented'
    )
    
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
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
    
    _max_content_show = 75
    def __str__(self) -> str:
        return truncatechars(self.content, Comment._max_content_show)