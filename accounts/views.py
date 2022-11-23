from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, "Logged in Successfully")
			return redirect('dashboard')
		else:
			messages.error(request, "Invalid Credentials")
			return redirect('login')

	return render(request, 'accounts/login.html')

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		con_password = request.POST['password2']
	
		if password == con_password:
			if not User.objects.filter(username=username).exists():
				if not User.objects.filter(email=email).exists():
					user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
					user.save()
					messages.success(request, "Account Created Successfully.")
					return redirect('login')
				else:
					messages.error(request, "This E-mail is already in use.")
					return redirect('register')
			else:
				messages.error(request, "This Username is already taken.")
				return redirect('register')
		else:
			messages.error(request, "The Passwords does not match.")
			return redirect('register')
			
	return render(request, 'accounts/register.html')

def logout(request):
	if request.method == "POST":
		auth.logout(request)
		messages.success(request, "Logged out Successfully.")
		return redirect('index')

def dashboard(request):
	contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	context = {
		'contacts': contacts
	}
	return render(request, 'accounts/dashboard.html', context)
