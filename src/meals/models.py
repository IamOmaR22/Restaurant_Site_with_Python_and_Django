from django.db import models
from django.utils.text import slugify

# Create your models here.

class Meals(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    people = models.IntegerField()  # This meal would be enough for how many people
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.IntegerField()   # The time this meal to be prepared
    image = models.ImageField(upload_to='meals/')   # The image for this meal.
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name: # When there is no slug but there is a name then we need to create the slug from the name.
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'meal'              # This is the singular name
        verbose_name_plural = 'meals'      # This is the plural name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'category'              # This is the singular name
        verbose_name_plural = 'categories'      # This is the plural name

    def __str__(self):
        return self.name
