# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm





class User(AbstractUser):


    GENDER_CHICE=[
        ('M','Male'),
        ('F','Female')
    ]
    COUNTRY_CHOICE=[
        ('IN','Indai')
    ]
    phone_number=models.CharField(max_length=15)
    profile_photo=models.ImageField(upload_to='uplodes/')
    dob=models.DateField(blank=True,null=True)
    bio=models.TextField(max_length=500,blank=True,null=True)
    job_title=models.CharField(max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=50,choices=GENDER_CHICE,default="M")
    country=models.CharField(max_length=20,choices=COUNTRY_CHOICE)
    open_to_hiring=models.BooleanField(default=False)


class Address(models.Model):
    id=models.BigAutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    Address_line_1=models.TextField(max_length=250)
    Address_line_2=models.TextField(max_length=250)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    is_default= models.BooleanField(default=True)

    class Meta:
        unique_together=['user','name']

    def __str__(self):
        return f'''(self.Address_line_1)
        {self.Address_line_2}'''