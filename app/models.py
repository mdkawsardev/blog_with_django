from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='media', blank=True, default='project1.png')
    description = models.TextField()