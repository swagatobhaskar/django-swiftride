from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    # i added first_name field
    first_name = forms.CharField(max_length=25, required=True)
    # i added last_name field
    last_name = forms.CharField(max_length=25, required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2',) # i added 'first_name','last_name'.
