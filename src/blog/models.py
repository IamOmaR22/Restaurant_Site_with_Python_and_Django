from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    created  = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ' post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title



class Category(models.Model):
    category_name = models.CharField(max_length=150)


    class Meta:
        verbose_name = ' category'
        verbose_name_plural = 'catogires'

    def __str__(self):
        return self.category_name