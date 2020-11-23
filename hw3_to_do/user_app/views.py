from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username = username, password = password)

            if not user is None:
            	login(request, user)
            messages.add_message(request, messages.SUCCESS, "User is created successfully.")
            return redirect("home")
        else:
            messages.add_message(request, messages.WARNING, "User is not created successfully")
    return render(request, 'registration/user_register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'registration/profile.html')

def user_logout(request):
	return render(request, 'registration/logout.html')







