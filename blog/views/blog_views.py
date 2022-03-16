from django.views.generic import ListView, DetailView
from blog import models

class BlogListView(ListView):
    model = models.Blog
    
class BlogDetailView(DetailView):
    model = models.Blog