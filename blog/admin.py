from django.contrib import admin
from django.contrib.auth import models as auth_models
from . import models

admin.site.register(auth_models.Permission)

@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'application_date_time',
        'status'
    )

@admin.register(models.Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio'
    )

class CommentInline(admin.TabularInline):
    model = models.Comment

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
    
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'to_str',
        'post_date',
        'commenter',
        'blog'
    )
    
    @admin.display(ordering='content', description='Comment')
    def to_str(self, obj):
        return str(obj)
