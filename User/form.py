from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#registration form database creation for user
class UserRegisteration(UserCreationForm):
    email = forms.EmailField()   # email  id of the user
    first_name = forms.CharField(max_length=100)  # first name of the user
    last_name = forms.CharField(max_length=100,)  # Last name of the user

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2'] # Fields for user registration
