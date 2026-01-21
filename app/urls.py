from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
    path('details/<int:pk>/', views.details, name='details'),
    path('category/', views.category, name='category'),
]
