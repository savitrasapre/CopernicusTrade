from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:symbol_name>/<str:update_type>", views.update, name='update'),
]