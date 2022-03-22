from re import template
from django.contrib.auth.models import User
from django.views.generic import DetailView, View, FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserDetailView(UserPassesTestMixin, DetailView):
    model = User
    template_name = 'blog/user_detail.html'
    
    def test_func(self):
        user = self.get_object()
        return user == self.request.user or 'auth.view_user' in self.request.user.get_all_permissions()
    
class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'is_active')
    template_name = 'blog/user_form.html'
    
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        user = self.get_object()
        if user != self.request.user:
            self.fields = ('is_active', )
    
    def get_success_url(self):
        view_name = 'blog:profile'
        # No need for reverse_lazy here, because it's called inside the method
        return reverse(view_name, kwargs={'pk': self.object.id})

    # only the user themselves can edit
    # the person who can delete users can also edit, but only is_active part, it's taken care of in setup(...)
    def test_func(self):
        user = self.get_object()
        return user == self.request.user or 'auth.delete_user' in self.request.user.get_all_permissions()
    
class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/user_confirm_delete.html'

    # only the original author and a moderator (or anyone having a perm to delete users) can delete
    def test_func(self):
        user = self.get_object()
        return user == self.request.user or 'auth.delete_user' in self.request.user.get_all_permissions()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required')
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
    
class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)