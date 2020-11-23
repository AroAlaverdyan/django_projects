from django.shortcuts import render, redirect
from .models import NewToDo
from .forms import TaskForm
# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages



def home(request):
	if not request.user.is_authenticated:
		return render(request, 'to_do/welcome.html')
	else:
		tasks = NewToDo.objects.all().filter(user = request.user)
		context = {
					'tasks': tasks
				}
		return render(request, 'to_do/home.html', context)

def to_do_view(request, pk):
	task = NewToDo.objects.get(id = pk)
	context = {'task':task}
	return render(request, 'to_do/task_view.html', context)

	
@login_required(login_url = 'login')
def to_do_update(request, pk):
	task = NewToDo.objects.all().filter(id = pk)[0]

	if request.method == "POST":
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Content updated successfully.")
			return redirect("home")
	
	form = TaskForm(instance = task)

	context = {'form': form}

	return render(request, 'to_do/task_update.html', context)

# class Create(CreateView):
# 	model = NewToDo
# 	fields = ['name', 'description']

@login_required(login_url = 'login')
def to_do_create(request):

	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit = False)
			task.user = User.objects.get(id = request.user.id)
			task.save()
			messages.add_message(request, messages.SUCCESS, "Content created successfully.")
			return redirect("home")
	
	form = TaskForm()

	context = {'form': form}

	return render(request, 'to_do/new_task.html', context)

@login_required(login_url = 'login')
def task_delete(request, pk):
	task = NewToDo.objects.get(id=pk)

	task.delete()
	messages.add_message(request, messages.WARNING, "Content already don't exist.")
	return redirect('home')


