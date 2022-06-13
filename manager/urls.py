from django.urls import path
from . import views


app_name = 'manager'
urlpatterns = [
    path('<username>/', views.index, name='index'),
    path('<username>/scanner/', views.scanner, name='scanner'),
    path('<username>/create/', views.create, name='create'),
]
