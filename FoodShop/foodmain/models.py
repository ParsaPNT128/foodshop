from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=18)
    phone = models.CharField(max_length=15, default = '', blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=40)
    ingredients = models.CharField(max_length=1000, default='', blank=True)
    picture = models.ImageField(upload_to='upload/course/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    ratings = models.FloatField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return self.name + ': ' + str(self.price)