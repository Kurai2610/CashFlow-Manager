from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                return render(request, 'signup.html', {'form': UserCreationForm(), 'message': 'User created successfully'})
            except:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'message': 'Username already exists'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'message': 'Passwords did not match'})
    else:
        return render(request, 'signup.html', {'form': UserCreationForm()})
