from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import Meals, Category

class MealsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)