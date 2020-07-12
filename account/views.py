from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		try:
			user = auth.authenticate(username=User.objects.get(email=email), password=password)
		except:
			messages.info(request, 'Invalid username or password')
			return redirect("login")
		
		if user is not None:
			auth.login(request, user)
			return redirect("/ranking/card")
		
		else:
			messages.info(request, 'Invalid username or password')
			return redirect("login")
		
	if request.method == 'GET':
		return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:

            if User.objects.filter(email=email.lower()).exists():
                messages.info(request, 'Email Address Alreasy Exist')
                return redirect('signup')

            elif User.objects.filter(username=user_name.lower()).exists():
                messages.info(request, 'Username Alreasy Exist')
                return redirect('signup')

            else:
                user = User.objects.create_user(
                    username=user_name.lower(),
                    password=password1,
                    email=email.lower(),
                    first_name=first_name.lower(),
                    last_name=last_name.lower()
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, "signup.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def profile(request):
	return render(request, "profile.html")


