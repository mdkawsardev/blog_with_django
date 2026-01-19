from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
    path('details/', views.details, name='details'),
]