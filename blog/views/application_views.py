from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView
from blog import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ApplicationCreateView(CreateView):
    model = models.Application
    fields = ('motivation',)

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'blogger') or \
            request.user.application_set.filter(status='w').exists():
            return render(request, 'blog/no_application.html') 
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
