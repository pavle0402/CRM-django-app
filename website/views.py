from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistrationForm


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back {username}. It's nice to see you again!")
            return redirect('home')
        else:
            messages.info(request, "There was an error with your login information. Please try again.")
            return redirect('home')
    else: 
        return render(request, 'home.html', {})

#here i made a little mistake by naming function logout(same as built in function) so i got error maximum reccursion depth exceeded. Probably
#meaning that i can't name my custom function like built in function and then use built in function inside of it.
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully completed your registration.")
            return redirect('home')            
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form":form})
