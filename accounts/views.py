from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()   # If the form is valid, a User instance is created with the user = form.save()
            login(request,user)
            # return redirect('home')
            return redirect('plan_select')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
