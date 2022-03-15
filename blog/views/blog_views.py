from django.views.generic import ListView
from blog import models

class BlogListView(ListView):
    model = models.Blog