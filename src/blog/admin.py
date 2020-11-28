from django.contrib import admin
from .models import Post, Category, Comment

from django_summernote.admin import SummernoteModelAdmin

class BlogPostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'

    list_display = ['title', 'author', 'category', 'created']
    search_fields = ['title', 'content']
    list_filter = ['category', 'tags']

admin.site.register(Post, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
