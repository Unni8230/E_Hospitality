from django.shortcuts import render, redirect
from . import urls
import bcrypt
from Hospital.models import *
from django.contrib import messages
# Create your views here.

def homePage(request):
    return render(request, 'homePage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Credentials.objects.filter(username=username).first()
        if user is not None:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                if user.type == "Patient":
                    request.session['user_id'] = user.id
                    return redirect('userprofile')
                elif user.type == "Doctor":
                    request.session['user_id'] = user.id
                    return redirect('doctorprofile')
                elif user.type=="Admin":
                    request.session['user_id'] = user.id
                    return redirect('adminprofile')
            else:
                messages.error(request,"Invalid Password!")
                return redirect('login')
        else:
            messages.error(request,"Invalid User!")
            return redirect('login')
    return render(request,'loginPage.html')
def logout(request):
    request.session.flush()
    return redirect('login')