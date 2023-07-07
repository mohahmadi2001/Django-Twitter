from typing import Any, Dict
from django import forms
from .models import User
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
    username = forms.CharField(
        widget=forms.TextInput({"class":"form-control"}),
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True
    )

    def clean(self) -> Dict[str, Any]:
        clean_data = super().clean()
        user = authenticate(
            self.request,
            username=clean_data["username"],
            password=clean_data["password"]
            )
        if user is not None:
            clean_data["user"] = user
            return clean_data
        else:
            raise forms.ValidationError("credential is invalid")


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True,
        label="کلمه عبور"
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput({"class":"form-control"}),
        required=True,
        label="تکرار کلمه عبور"
        )
    class Meta:
        model = User
        fields={
            "username",
            "password1",
            "password2",
            "age",
            "bio",
            "image",
        }
        widget={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "bio":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.ImageField(attrs={"class":"form-control"}),
        }
        
    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        password1 = cleaned_data.pop('password1', None)
        password2 = cleaned_data.pop('password2', None)
        if password1 != password2:
            self.add_error('password2', forms.ValidationError(
                'در وارد کردن کلمه عبور دقت کنید', code='invalid'))
            cleaned_data.setdefault('password', password1)
        return cleaned_data
    
    def save(self, commit: bool = ...) -> Any:
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserEditInfo(forms.ModelForm):
    
    class Meta:
        model = User
        fields={
            "username",
            "password",
            "bio",
            "image",
        }
        widget={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "bio":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.ImageField(attrs={"class":"form-control"}),
        }
        

    