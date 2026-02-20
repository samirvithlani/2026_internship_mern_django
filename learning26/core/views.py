from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib.auth import login
# Create your views here
# .

def registerUser(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            #is_staff = true
            form.save()
            #auto login..
            # user = User.objects.get(username=form.cleaned_data['username'])
            # login(request,user)
            return redirect('employeeList')
    else:
        form = UserForm()
        return render(request,'core/register.html',{'form':form})
