from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        print("form")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form valid")
            form.save()
            username = form.cleaned_data.get('username')
            # username = 's'
            messages.success(request, f'Account created for {username}')
            return redirect('home')
            # return HttpResponse('resp')
        else:
            # return "neh"
            print ("neh")
            pass
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render (request, 'users/profile.html')
