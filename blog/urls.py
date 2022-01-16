from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('create_post/', views.create_post, name='createpost'),
    path('edit_post/', views.edit_post, name='editpost'),
    path('view_post/', views.view_post, name='viewpost'),
    path('delete_post/', views.delete_post, name='deletepost'),
    path('', views.dashboard, name='dashboard'),
]