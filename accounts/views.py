from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def login(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		try:
			user = auth.authenticate(username=User.objects.get(email=email), password=password)
		except:
			messages.info(request, 'Invalid email address or password')
			return redirect("login")
		
		if user is not None:
			auth.login(request, user)
			return redirect("/ranking/card")
		
		else:
			messages.info(request, 'Invalid email address or password')
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
        institution = request.POST.get('institution')
        level = request.POST.get('level')

        if password1 == password2:
            if User.objects.filter(email=email.lower()).exists():
                messages.info(request, 'Email Address Alreasy Exist')
                return redirect('signup')
                
            else:
                user = User.objects.create_user(
                    username=user_name.lower(),
                    password=password1,
                    email=email.lower(),
                    first_name=first_name.lower(),
                    last_name=last_name.lower(),
                    institution=institution.lower(),
                    level=level.lower()
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        profile = User.objects.all().last()
        return render(request, "signup.html", {"profile": profile})


def contact(request):
    if request.method == "POST":
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_phone = request.POST['contact_phone']
        contact_message = request.POST['contact_message']
        subject = 'Journal Ranker Message from ' + contact_name
        message = f"Name: {contact_name} \nEmail: {contact_email} \nMessage: {contact_message}"
        #recipients = [settings.EMAIL_HOST_USER]
        recipients = ['journalranker@gmail.com',]
        try:
            send_mail(subject, message, contact_name, recipients) #, fail_silently=True)
        except BadHeaderError:
            messages.info(request, 'Invalid header found')
            return HttpResponse('Invalid header found')
    
        return render(request, "contact.html", {'contact_name': contact_name})

    if request.method == "GET":
        return render(request, "contact.html")


@login_required
def profile(request):
	return render(request, "profile.html")


@login_required  
def logout(request):
    auth.logout(request)
    return redirect("/")




