from django.urls import path
from . import views
# from .views import Create


urlpatterns = [
    path('', views.home, name = 'home'),
    path('to_do_view/<str:pk>', views.to_do_view, name = 'to_do_view'),
    path('to_do_update/<str:pk>', views.to_do_update, name = 'to_do_update'),
    path('to_do_create/', views.to_do_create, name = 'to_do_create'),
    path('task_delete/<int:pk>', views.task_delete, name = 'task_delete'),
    # path('to_do_create/', Create.as_view(), name = 'to_do_create'),
]