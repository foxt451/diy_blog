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
    path('applications/', views.ApplicationAllListView.as_view(), name='applications'),
    path('applications/pending/', views.ApplicationPendingListView.as_view(), name='applications-pending'),
    path('profile/<int:pk>/applications/', views.ApplicationUserListView.as_view(), name='applications-of-user'),
    path('application/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application-delete'),
    path('application/<int:pk>/edit/', views.ApplicationUpdateView.as_view(), name='application-edit'),
    path('application/<int:pk>/reject/', views.ApplicationRejectView.as_view(), name='application-reject'),
    path('application/<int:pk>/accept/', views.application_accept, name='application-accept'),
    
    path('blog/<int:blog_pk>/comment-create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    
    path('garbage/', views.garbage, name='garbage')
]
