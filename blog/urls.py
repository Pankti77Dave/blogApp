
from xmlrpc.client import Boolean
from django.urls import path
from . import views
from .views import BlogDetail, BlogSearch, BlogAdd


urlpatterns = [
    path('search/', BlogSearch.as_view(), name='search'),
    path('add/', BlogAdd.as_view(), name='add'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('<int:post_id>/createcomment/', views.comment_add, name='createcomment'),
    path('<int:post_id>/commentdelete/<int:id>/',views.comment_delete, name='deletecomment'),
    path('<int:id>/', BlogDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.tag, name='tag_detail'),
] 