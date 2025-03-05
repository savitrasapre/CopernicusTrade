from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login/<str:username>/<str:password_hash>", views.login, name='login'),
    path("register/<str:username>/<str:email>/<str:password_hash>", views.register, name='register'),
    path("<str:echo_str>/echo", views.echo, name='echo')
]