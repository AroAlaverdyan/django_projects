from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from datetime import datetime

# Create your views here.

def greeting(request):
	return HttpResponse('<img src=https://www.eurodiaconia.org/wordpress/wp-content/uploads/2016/02/welcome.jpg />')

def introduction(request):
	return HttpResponse("<h1><b>This is Aro's website<b><h1>\
		<hr>\
		<h3><i>Soon this site will become more attractive and useful</i><h3>\
		<h4><p style=background-color:LightSlateGray;>If you see this message it means that I'm on the right track and I'll do my best to create my First website!!! </h4></p>")

def date_time(request):
	today = date.today()
	now = datetime.now().time()
	
	return HttpResponse(f"Today's date: {today} Time: {now}")

def square_num(request):
	my_dict = {}
	for i in range(1,16):
		my_dict.setdefault(i, i**2)
	return HttpResponse(f"{my_dict}")
