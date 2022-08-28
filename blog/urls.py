
from django.urls import path
from . import views



urlpatterns = [
    path('search/', views.search, name='search'),
    path('add/', views.add, name='add'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('<int:post_id>/createcomment/', views.comment_add, name='createcomment'),
     path('<int:post_id>/commentdelete/<int:id>/',views.comment_delete, name='deletecomment'),
    path('<int:id>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.tag, name='tag_detail'),
] 