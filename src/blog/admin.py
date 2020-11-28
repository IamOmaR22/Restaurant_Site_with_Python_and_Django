from django.contrib import admin
from .models import Post, Category, Comment

from django_summernote.admin import SummernoteModelAdmin

class BlogPostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
