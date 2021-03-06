from django.db import models
from .blogger import Blogger
from django.urls import reverse
from django.template.defaultfilters import truncatechars

class Blog(models.Model):
    class Meta:
        ordering = ('-post_date',)
    
    post_date = models.DateTimeField(
        'Posted',
        auto_now_add=True,
        help_text='The time when the blog is created'
    )
    
    author = models.ForeignKey(
        Blogger,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        help_text='Author of the blog'
    )
    
    title = models.CharField(max_length=100, help_text='Blog\'s title')
    content = models.TextField(max_length=10_000, help_text='Blog\'s content')
    
    _max_title_show = 50
    
    def __str__(self) -> str:
        shortened_title = truncatechars(self.title, Blog._max_title_show)
        return f'(by {a if (a:=self.author) else "[deleted]"} | {self.post_date.strftime("%x %X")}) {shortened_title}'
    
    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=(self.id,))