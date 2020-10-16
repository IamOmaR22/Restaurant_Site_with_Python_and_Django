from django.db import models

# Create your models here.

class Meals(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700)
    people = models.IntegerField()  # This meal would be enough for how many people
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.IntegerField()   # The time this meal to be prepared
    image = models.ImageField(upload_to='meals/')   # The image for this meal.


    def __str__(self):
        return self.name
