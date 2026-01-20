from django.contrib import admin
from .models import Category, Select, Post, Number
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
admin.site.register(Select)
admin.site.register(Post)
admin.site.register(Number)