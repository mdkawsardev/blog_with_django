from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/', views.post, name='post'),
    path('details/<uuid:unique_code>/', views.details, name='details'),
    path('category/', views.category, name='category'),
    path('analyze/', views.analyze, name='analyze'),
    path('edit/', views.edit, name='edit'),
]
