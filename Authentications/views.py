from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView,View,UpdateView,TemplateView,FormView
from django.urls import reverse,reverse_lazy
from .forms import *
from .models import User,Address
from django.http import HttpResponse
from django.shortcuts import render




class login(View):
    form_class= LoginForm
    template_name = 'jobPortal/login.html'

    def get(self,request, *args,**kwargs):
        return render (request,self.template_name,{'form':self.form_class()})
    
    def post(self,request,*args, **kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Incalid username or passord")
        return render(request,self.template_name,{'form':form})


class RegisterView(View):
    form_class=UserCreationForm
    template_name='jobportal/register.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class()})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{'form':form})
        
        user=form.save(commit=False)
        user.password=form.cleaned_data=['password']
        user.save()
        return redirect('login')
            
               