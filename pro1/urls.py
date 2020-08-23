from pro1 import views
from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns=[
    path('home',views.home,name='home'),
    path('Login/',LoginView.as_view(),name='Login'),
    path('item/<str:subcategory>/',views.item,name='item'),
    path('category/<str:subcategory>/<str:search>',views.categorysearch,name='categorysearch'),
    path('profile',views.profile,name='Profile'),
    path('search',views.search,name='Search')
    ]