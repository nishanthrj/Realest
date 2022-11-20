from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def login(request):
	if request.method == 'POST':
		messages.error(request, 'Testing')
		return redirect('login')
	return render(request, 'accounts/login.html')

def register(request):
	return render(request, 'accounts/register.html')

def logout(request):
	return redirect('index')

def dashboard(request):
	return render(request, 'accounts/dashboard.html')
