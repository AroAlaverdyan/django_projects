from django.shortcuts import render, redirect
from .models import NewToDo
from .forms import TaskForm
# from django.views.generic import CreateView


def home(request):
	tasks = NewToDo.objects.all()
	context = {
				'tasks': tasks
			}
	return render(request, 'to_do/home.html', context)

def to_do_view(request, pk):
	task = NewToDo.objects.all().filter(id = pk)[0]

	forms = TaskForm(instance = task)

	content = {
				'forms': forms,
				'task': task
				}

	return render(request, 'to_do/task_view.html', content)


def to_do_update(request, pk):
	task = NewToDo.objects.all().filter(id = pk)[0]

	if request.method == "POST":
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			form.save()
			return redirect("home")
	
	form = TaskForm(instance = task)

	context = {'form': form}

	return render(request, 'to_do/task_update.html', context)

# class Create(CreateView):
# 	model = NewToDo
# 	fields = ['name', 'description']

def to_do_create(request):

	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	
	form = TaskForm()

	context = {'form': form}

	return render(request, 'to_do/new_task.html', context)


def task_delete(request, pk):
	task = NewToDo.objects.get(id=pk)

	task.delete()
	return redirect('home')


