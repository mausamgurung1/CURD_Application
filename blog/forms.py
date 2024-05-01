from django import forms

from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'contact', 'address', 'gender', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
