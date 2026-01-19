from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='media', blank=True)
    description = models.TextField()