from django.urls import path
from . import views
from .views import BlogRegister, BlogLogin, BlogLogout
urlpatterns = [
    path('register/', BlogRegister.as_view(), name='register'),
    path('login/', BlogLogin.as_view(), name='login'),
    path('logout/',BlogLogout.as_view(),name='logout')
]