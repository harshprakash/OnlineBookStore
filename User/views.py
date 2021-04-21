from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisteration
#registertion of new user function
def register(request):
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"your account is created now you can login !")
            return redirect('Login')
    else:    
        form = UserRegisteration()
    return render(request,"User/registeration.html",{'form':form})


