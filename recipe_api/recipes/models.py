from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    DIET_CHOICES = [
        ('balanced', 'balanced'),
        ('high-protein', 'high-protein'),
        ('high-fiber', 'high-fiber'),
        ('low-sodium', 'low-sodium'),
        ('low-carb', 'low-carb'),
        ('low-fat', 'low-fat'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    time_mins = models.PositiveIntegerField()
    ingredients = models.ManyToManyField('Ingredient')
    diet = models.CharField(max_length=12, choices=DIET_CHOICES, default='balanced')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)