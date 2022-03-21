from ast import Del
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from blog import models
from django.urls import reverse

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = models.Comment
    fields = ('content',)
    
    def setup(self, request, *args, **kwargs):
        self.blog = get_object_or_404(models.Blog, id=kwargs['blog_pk'])
        super().setup(request, *args, **kwargs)
        
    def get_success_url(self) -> str:
        return reverse('blog:blog-detail', args=(self.blog.id,))
    
    def form_valid(self, form):
        form.instance.commenter = self.request.user
        form.instance.blog = self.blog
        return super().form_valid(form)
    
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = models.Comment
    
    def get_success_url(self) -> str:
        return reverse('blog:blog-detail', args=(self.object.blog.id,))
    
    def test_func(self):
        comment = self.get_object()
        return comment.commenter == self.request.user or 'blog.delete_comment' in self.request.user.get_all_permissions()