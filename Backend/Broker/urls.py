from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task', views.trigger_task, name='task'),
    path("<str:update_type>/<str:symbol_name>", views.update, name='update'),
]