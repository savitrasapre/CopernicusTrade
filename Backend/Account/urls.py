from django.urls import path
from . import views
from .views import AccountView, LoginView, RegisterView

urlpatterns = [
    path('', AccountView.as_view(), name='index'),
    path("login/<str:username>/<str:password_hash>", LoginView.as_view(), name='login'),
    path("register/<str:username>/<str:email>/<str:password_hash>", RegisterView.as_view(), name='register'),
    path("<str:echo_str>/echo", views.echo, name='echo')
]