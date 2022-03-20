from statistics import mode
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView, FormView
from blog import models
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from blog import models
from django import forms

from blog.models import application


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = models.Application
    fields = ('motivation', 'bio')

    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'blogger') or \
            (not request.user.is_anonymous and request.user.application_set.filter(status='w').exists()):
            return render(request, 'blog/no_application.html') 
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ApplicationDeleteView(UserPassesTestMixin, DeleteView):
    model = models.Application
    
    def get_success_url(self) -> str:
        return reverse('blog:applications-of-user', args=(self.object.user.id,))

    # only the original author and a moderator (or anyone having a perm to delete applications) can delete
    def test_func(self):
        application = self.get_object()
        return application.user == self.request.user or 'blog.delete_application' in self.request.user.get_all_permissions()
    
class ApplicationUpdateView(UserPassesTestMixin, UpdateView):
    model = models.Application
    fields = ('motivation', 'bio')

    # only the original author can edit
    def test_func(self):
        application = self.get_object()
        return application.user == self.request.user
    
class ApplicationAllListView(PermissionRequiredMixin, ListView):
    model = models.Application
    permission_required = 'blog.can_approve_application'

    def get_queryset(self):
        return models.Application.objects.all()
    
    def test_func(self):
        return 'blog.can_approve_application' in self.request.user.get_all_permissions()
    
class ApplicationUserListView(UserPassesTestMixin, ListView):
    model = models.Application

    def get_queryset(self):
        return models.Application.objects.filter(user__id=self.kwargs['pk'])
    
    def test_func(self):
        return 'blog.can_approve_application' in self.request.user.get_all_permissions() or self.request.user.id == self.kwargs['pk']
    
class ApplicationPendingListView(PermissionRequiredMixin, ListView):
    permission_required = 'blog.can_approve_application'
    model = models.Application

    def get_queryset(self):
        return models.Application.objects.filter(status='w')

class ApplicationDetailView(UserPassesTestMixin, DetailView):
    model = models.Application
    
    def test_func(self):
        application = self.get_object()
        return 'blog.can_approve_application' in self.request.user.get_all_permissions() or self.request.user == application.user
  
  
class ApplicationRejectForm(forms.Form):
    comment = forms.CharField(max_length=2000)
    
class ApplicationRejectView(PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.can_approve_application'
    
    template_name = 'blog/application_reject_form.html'
    model = models.Application
    fields = ('comment',)
    
    def get_success_url(self) -> str:
        return reverse('blog:application-detail', args=(self.object.id,))
    
    def form_valid(self, form):
        form.instance.status = 'r'
        return super().form_valid(form)
    
   
@permission_required('blog.can_approve_application')
def application_accept(request, pk):
    application = get_object_or_404(models.Application, id=pk)
    application.status = 'a'
    application.save()
    user = application.user
    # add an author for the user
    blogger = models.Blogger(bio=application.bio, user=user)
    blogger.save()
    return HttpResponseRedirect(reverse('blog:application-detail', args=(application.id,)))
