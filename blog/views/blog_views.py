from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog import models
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


class BlogListView(ListView):
    model = models.Blog

    def get_queryset(self):
        if (pk := self.kwargs.get('pk', None)) is not None:
            return models.Blog.objects.filter(author__id=pk)
        else:
            return models.Blog.objects.all()


class BlogDetailView(DetailView):
    model = models.Blog

class BlogCreateView(UserPassesTestMixin, CreateView):
    model = models.Blog
    fields = ('title', 'content')
    
    # any author can create a new blog
    def test_func(self):
        return hasattr(self.request.user, 'blogger')
    
    def form_valid(self, form):
        form.instance.author = self.request.user.blogger
        return super().form_valid(form)

class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = models.Blog
    fields = ('title', 'content')

    # only the original author can edit
    def test_func(self):
        blog = self.get_object()
        return blog.author is not None and blog.author.user == self.request.user


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = models.Blog
    success_url = reverse_lazy('blog:blogs')

    # only the original author and a moderator (or anyone having a perm to delete blogs) can delete
    def test_func(self):
        blog = self.get_object()
        return (blog.author is not None and blog.author.user == self.request.user) or 'blog.delete_blog' in self.request.user.get_all_permissions()

class GarbageForm(forms.Form):
    garbage_name = forms.CharField(max_length=100)
    garbage_age = forms.IntegerField(max_value=200, min_value=0)


def garbage(request):
    if request.method == 'POST':
        form = GarbageForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = GarbageForm({'garbage_age': 900})
    return render(request, 'blog/garbage.html', context={'form': form})
