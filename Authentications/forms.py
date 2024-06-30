from django.forms import EmailInput,ModelForm,Form,Select,RadioSelect,CharField
from django.forms import TextInput, PasswordInput,CharField,Textarea,FileInput
from django.core.validators import MinLengthValidator
from .models import *


class LoginForm(Form):
    username=CharField(
        max_length=15,
        min_length=4,
        required=True,
        label="Username",
        widget=TextInput({
            'class':'form-control'
        })
              )
    
    password=CharField(
        max_length=15,
        min_length=4,
        required=True,
        label='Password',
        widget=PasswordInput({
            'class':'form-control'
        })
    )

class UserCreationForm(ModelForm):
    confirm_password=CharField(
        max_length=25,
        min_length=8,
        required=True,
        validators=[
            MinLengthValidator(8,'The password is too short.')
        ],
        widget= PasswordInput({
            'class':'form-control'
        })

    )