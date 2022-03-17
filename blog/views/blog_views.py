from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


class BlogCreateView(CreateView):
    model = models.Blog
    fields = ('title', 'content')


class BlogUpdateView(UpdateView):
    model = models.Blog
    fields = ('title', 'content')


class BlogDeleteView(DeleteView):
    model = models.Blog
    success_url = reverse_lazy('blog:blogs')
    
from django import forms
    
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
