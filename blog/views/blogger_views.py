from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog import models
from django.urls import reverse_lazy, reverse

class BloggerListView(ListView):
    model = models.Blogger
    
class BloggerDetailView(DetailView):
    model = models.Blogger
    
class BloggerUpdateView(UserPassesTestMixin, UpdateView):
    model = models.Blogger
    fields = ('bio',)

    # only the blogger themselves can edit
    def test_func(self):
        blogger = self.get_object()
        return blogger.user == self.request.user
    
class BloggerDeleteView(UserPassesTestMixin, DeleteView):
    model = models.Blogger
    success_url = reverse_lazy('blog:bloggers')

    # only the original author and a moderator (or anyone having a perm to delete bloggers) can delete
    def test_func(self):
        blogger = self.get_object()
        return blogger.user == self.request.user or 'blog.delete_blogger' in self.request.user.get_all_permissions()