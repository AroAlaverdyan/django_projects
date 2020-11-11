from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.jsonfile, name='jsonfile'),
    path('dict/', views.my_dict, name='my_dict'),
    path('authentication/', views.auto, name='auto'),
]
