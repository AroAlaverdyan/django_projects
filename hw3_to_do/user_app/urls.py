from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name = "login"),
    path('logoutbasic/',auth_views.LogoutView.as_view(), name="logoutbasic"),
    path('register/', user_views.user_register, name = "register"),
    path('profile/', user_views.profile, name = "profile"),
    path('user_logout/', user_views.user_logout, name = "user_logout"),
]