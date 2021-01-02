from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('realestate', views.about, name='about'),
    path('about', views.about, name='about'),
]