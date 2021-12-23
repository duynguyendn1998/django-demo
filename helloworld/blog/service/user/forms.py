from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    #Create form input user infor
    username = forms.CharField(label='User name', max_length=30) # max_length=30: Cannot enter to than 30 character, label='User name': this field display label 'User name' in UI
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())# widget=forms.PasswordInput(): The field is password, hidden input value
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput()) 

    def clean_password2(self): # method check password and password confirm 
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Password is incorrect")

    def clean_username(self): 
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username): # Do the username check contains special characters?
            raise forms.ValidationError("User name with special characters")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist: # Check user has been exist?
            return username
        raise forms.ValidationError("User name already exists")

    def save(self): #Save user info to auth_user table of django
        User.objects.create_user(username=self.cleaned_data['username'], 
        email=self.cleaned_data['email'], 
        password=self.cleaned_data['password1'],
        first_name = self.cleaned_data['first_name'],
        last_name = self.cleaned_data['last_name'],)
