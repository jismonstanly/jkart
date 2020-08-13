from django.urls import path
import jk.views

urlpatterns=[
    path('login',jk.views.login,name='login'),
    path('index',jk.views.index,name='index'),
    path('',jk.views.index,name='index'),
    path('registration',jk.views.registration,name='registration'),
    path('category_fruits',jk.views.category_fruits,name='category_fruits'),
    path('category_vegetables',jk.views.category_vegetables,name='category_vegetables'),
]