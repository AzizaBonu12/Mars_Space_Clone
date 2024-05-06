from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password']


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
