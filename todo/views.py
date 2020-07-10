from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':"This User Name has been already taken, Please Chose another."})    
        else:
            #You are not enter the same password
            return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':"Password did not match"})



def logoutuser(request):
    if request.method == 'POST':
        pass




def currenttodos(request):
    return render(request, 'todo/currenttodos.html')