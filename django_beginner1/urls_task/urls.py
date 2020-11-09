from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.greeting, name='greeting'),
    path('introduction/', views.introduction, name='introduction'),
    path('date/', views.date_time, name='date_time'),
    path('dict/', views.square_num, name='square_num'),
    path('video/', views.video, name='video'),

]