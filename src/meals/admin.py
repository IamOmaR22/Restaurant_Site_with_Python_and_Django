from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Meals, Category

class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

    list_display = ['name', 'category', 'people', 'price', 'preparation_time']
    search_fields = ['name', 'description']
    list_filter = ['category', 'price']

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)