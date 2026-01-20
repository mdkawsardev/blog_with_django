from django.contrib import admin
from .models import Category, Select, Post, Number
# Register your models here.
admin.site.register(Category)
admin.site.register(Select)
admin.site.register(Post)
admin.site.register(Number)