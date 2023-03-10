from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm
from main.models import User


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class CreateUserForm(ModelForm):
    password1 = forms.CharField(
        label="Password",
        help_text=password_validation.password_validators_help_text_html(),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        help_text="Enter the same password as before for validation",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ["email", 'username']

    def username_clean(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError(" Username Already Exist")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


