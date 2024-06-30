# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import Permission
# from phonenumber_field.modelfields import PhoneNumberField

# class ProfileData(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254, unique=True)
#     phone_number = PhoneNumberField()
#     age = models.IntegerField()
    
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     location = models.CharField(max_length=50)
#     experience = models.IntegerField()
#     profile_img = models.ImageField(upload_to='uploads/')
#     cv = models.FileField(upload_to='uploads/')

#     def __str__(self):
#         return self.name

# class Skill(models.Model):
#     profile = models.ForeignKey(ProfileData, on_delete=models.CASCADE, related_name='skills')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Certification(models.Model):
#     profile = models.ForeignKey(ProfileData, on_delete=models.CASCADE, related_name='certifications')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Language(models.Model):
#     profile = models.ForeignKey(ProfileData, on_delete=models.CASCADE, related_name='languages')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Qualification(models.Model):
#     profile = models.ForeignKey(ProfileData, on_delete=models.CASCADE, related_name='qualifications')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name






class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name='authentications_user_set'  # Ensure this is unique
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name='authentications_user_permissions_set'  # Ensure this is unique
    )


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