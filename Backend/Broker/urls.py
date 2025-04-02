from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:update_type>/<str:strategy_type>/<str:symbol_name>", views.update, name='update'),
]