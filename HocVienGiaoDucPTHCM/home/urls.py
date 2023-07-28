from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('courses/', views.courses),
    path('about/', views.about),
    path('blog/', views.blog),
    path('blog_details/', views.blog_details),
    path('elements/', views.elements),
    path('contact/', views.contact),
    path('login/', views.login),
    path('register/', views.register),
    path('new', views.new),
    path('loginacc', views.loginacc),
    path('savepost', views.savepost),
    path('pay/', views.pay),
    path('service/', views.service)
]
