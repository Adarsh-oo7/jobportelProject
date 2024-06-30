from django.urls import path
from  .views import *
urlpatterns = [
    path('',login.as_view(),name='login'),
    path('reg',RegisterView.as_view(),name='register')
  
]
