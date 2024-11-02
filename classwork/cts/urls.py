from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/<int:pk>', views.record, name='record'),
    path('create_city/', views.create, name='create'),
    path('update_city/<int:pk>', views.update, name='update'),
    path('delete_city/<int:pk>', views.delete, name='delete')
]
