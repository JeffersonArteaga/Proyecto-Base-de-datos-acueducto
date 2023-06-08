from django import forms
from django.forms import ModelForm

from user.models import User


class FormUser(ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','tipo', 'password')
        widgets = {

        }

class Meme():
    pass