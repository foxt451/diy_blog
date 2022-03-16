from django.views.generic import ListView, DetailView
from blog import models

class BloggerListView(ListView):
    model = models.Blogger
    
class BloggerDetailView(DetailView):
    model = models.Blogger