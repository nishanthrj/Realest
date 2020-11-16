from django.shortcuts import render
from django.http import HttpResponse

def index(response):
		return render(response, 'pages/index.html')



def about(response):
	return render(response, 'pages/about.html')
