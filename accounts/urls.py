from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', views.index2, name='index2'),
    path('register/', views.register, name='register')
]