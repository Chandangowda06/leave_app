from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import Http404
from django.views.decorators.http import require_POST



def index(request):
    return render(request, 'index.html')

def profile(request):
    authenticated = request.session.get('authenticated', False)
    username = request.session.get('username', None)
    if authenticated:
        if username != None:
            staff = User.objects.get(username=username)
            staff_profile = StaffDetail.objects.get(staff=staff)
            if staff_profile:
                return render(request, 'profile.html', {'staff':staff_profile})
    raise Http404("Page not found")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['authenticated'] = True
            request.session['username'] = user.username
            return redirect('profile')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def apply(request):
    return render(request, 'apply.html')

def update(request):
    return render(request, 'update.html')

def leave_requests(request):
    return render(request, 'leave.html')