from django.urls import path
from blog import views
from blog.views.blog_views import BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(),
         name='blogger-detail'),
    path('blogger/<int:pk>/blogs/', views.BlogListView.as_view(),
         name='blogs-of-blogger'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),

    path('blog/publish/', views.BlogCreateView.as_view(), name='blog-publish'),
    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog-edit'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
    
    path('blogger/<int:pk>/edit/', views.BloggerUpdateView.as_view(), name='blogger-edit'),
    path('blogger/<int:pk>/delete/', views.BloggerDeleteView.as_view(), name='blogger-delete'),
    
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', views.UserUpdateView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/delete/', views.UserDeleteView.as_view(), name='profile-delete'),
    
    path('application/create/', views.ApplicationCreateView.as_view(), name='application-create'),
    
    path('garbage/', views.garbage, name='garbage')
]
