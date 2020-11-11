from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.

with open("sample_json.json", "r") as f:
	file = json.load(f)

def jsonfile(request):
	context = {"items": file}
	return render(request, 'app_template_2/jsonfile.html', context)



d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for i in d2:
	if i in d1:
		a = d2[i]+d1[i]
		d1.update({i:a})
	else:
		d1.update({i: d2[i]})

def my_dict(request):
	context = {
				"name": d1
				}

	return render(request, "app_template_2/my_dict.html", context)

def auto(request):
	
	return render(request, 'app_template_2/authentication.html')


