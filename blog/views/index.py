from django.shortcuts import render
from blog import models


def index(request):
    return render(request, 'blog/index.html',
                  context={'pending_applications':
                           models.Application.objects.filter(status='w',
                                                             user=request.user)}
                  if not request.user.is_anonymous else {})
