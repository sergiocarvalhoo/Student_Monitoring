from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import UserModelForm

# Create your views here.


def register(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login')
    return render(request, 'register.html', context)


def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/ifpb/students')
    return render(request, 'login.html')


def do_logout(request):
    logout(request)
    return redirect('/')
