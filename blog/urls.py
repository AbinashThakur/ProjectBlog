from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('create_post/', views.create_post, name='createpost'),
    path('edit_post/', views.edit_post, name='editpost'),
    path('delete_post/', views.delete_post, name='deletepost'),
    path('', views.dashboard, name='dashboard'),
]