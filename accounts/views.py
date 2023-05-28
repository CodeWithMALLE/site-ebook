from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.

User = get_user_model()


def signup(request):
	if request.POST:
		# traiter le formaulaire
		username = request.POST["username"]
		password = request.POST["password"]
		user = User.objects.create_user(username=username, password=password)

		login(request, user)
		return redirect("index")

	return render(request, 'accounts/signup.html')


def login_user(request):
	if request.POST:
		# connecter l'utilisateur
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect("index")
	return render(request, 'accounts/login.html')


def logout_user(request):
	logout(request)
	return redirect("index")
