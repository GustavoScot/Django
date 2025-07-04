from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
]