from django.shortcuts import render
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeForm,update_session_auth_hash 
from django.contrib.auth.views import LoginView

# Create your views here.

@login_required(login_url='/users/login')
def Profile(request):
	context = {}
	return render(request, 'Profile.html',context)

def Register(request):
	context = {}
	return render(request, 'Register.html',context)

def Login(request):
	context = {}
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,email=email, password=password)
		if user is not None:
			login(request,user)
			return redirect(request.GET.get('next','/'))
	return render(request, 'Login.html',context)

@login_required(login_url='/users/login')
def Logout(request):
	return redirect('login')

@login_required(login_url='/users/login')
def EditProfile(request):
	context = {}
	return render(request, 'EditProfile.html',context)

