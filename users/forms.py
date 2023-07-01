from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import GeekUser

class UserRegistrationForm(UserCreationForm):
    #password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    #password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают.")
        return cd['password2']

class GeekUserCreationForm(UserCreationForm):
    class Meta:
        model = GeekUser
        fields = ["email"]

class GeekUserChangeForm(UserChangeForm):
    class Meta:
        model = GeekUser
        fields = ["email"]