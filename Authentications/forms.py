from django.forms import EmailInput,ModelForm,Form,Select,RadioSelect,CharField
from django.forms import TextInput, PasswordInput,CharField,Textarea,FileInput,CheckboxInput
from django.core.validators import MinLengthValidator
from .models import *
from django.contrib.auth.models import User

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

    class Meta:
        models=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone',
            'profile_photo',
            'dob',
            'short_bio',
            'job_title',
            'gender',
            'country',
            'open_to_hiring'
        ]

        widgets = {
            'username': TextInput({
                'class': 'form-control'
            }),

            'email': EmailInput({
                'class': 'form-control'
            }),
            
            'first_name': TextInput({
                'class': 'form-control'
            }),

            'last_name': TextInput({
                'class': 'form-control'
            }),
            
            'password': PasswordInput({
                'class': 'form-control'
            }),

            'phone': TextInput({
                'class': 'form-control'
            }),

            'dob': TextInput({
                'class': 'form-control'
            }),

            'short_bio': Textarea({
                'class': 'form-control',
                'rows': '3'
            }),

            'job_title': TextInput({
                'class': 'form-control',
            }),

            'gender': Select({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),

            'open_to_hiring': CheckboxInput(),

            'profile_photo': FileInput({
                'class': 'form-control'
            })
        }
