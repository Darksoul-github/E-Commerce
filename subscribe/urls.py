from django.urls import path
from subscribe import views
 
urlpatterns=[
    path('Email',views.email,name='Email'),
    ]