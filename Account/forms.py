from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.forms import widgets
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):

    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username == 'admin':
            messages.add_message(self.request, messages.SUCCESS, "Hoş geldin, admin")
        
        return username
        

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['email'].required = True
        self.fields['first_name'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['first_name'].required = True
        self.fields['last_name'].widget = widgets.EmailInput(attrs={'class': 'form-control'})
        self.fields['last_name'].required = True
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email bilgisi başka bir hesapla eşleşiyor.')
        
        return email
    

class PasswordChangeUserForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
