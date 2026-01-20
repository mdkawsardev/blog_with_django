from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='media', blank=True, default='project1.png')
    description = models.TextField()

class Select(models.Model):
    select = models.ForeignKey(Category, on_delete=models.CASCADE)
