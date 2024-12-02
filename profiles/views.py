from django.shortcuts import render,redirect
from rest_framework import generics
from rest_framework.response import Response
from django.views import View
from .serializers import profile_serializer,project_serializer
from .models import profile,project
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import add_project
from django.contrib import messages
from django.contrib.auth.models import auth
from rest_framework.permissions import IsAuthenticated, AllowAny
import json
import urllib

# Create your views here.

class profilesAPI(generics.CreateAPIView,generics.ListAPIView, generics.DestroyAPIView,generics.UpdateAPIView):
    serializer_class = profile_serializer
    lookup_field = 'username'
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'id' in self.kwargs:
            return profile.objects.filter(id=self.kwargs['id'])
        if 'username' in self.kwargs:
            return profile.objects.filter(username=self.kwargs['username'])
        return profile.objects.all()
    
    def get_object(self):
        if 'id'in self.kwargs:
            return profile.objects.filter(id=self.kwargs['id'])
        if 'username' in self.kwargs:
            return profile.objects.filter(username = self.kwargs['username'])
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class projectsAPI(generics.ListAPIView,generics.CreateAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    serializer_class = project_serializer
    lookup_field = 'username'

    def get_object(self):
        return project.objects.get(id=self.kwargs['id'])
    
    def get_queryset(self):
        if 'id' in self.kwargs:
            return project.objects.get(id=self.kwargs['id'])
        if 'username' in self.kwargs:
            return project.objects.filter(username=self.kwargs['username'])
        return project.objects.all()
    
    def post(self,request,*args,**kwargs):
        serializer = project_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
class home(View):
    def get(self,request,*args,**kwargs):
        context = {
            "profiles" : json.loads(urllib.request.urlopen('http://127.0.0.1:8000/api/profiles').read()),
        }
        return render(request,'home.html',context)

class projects(View):
    def get(self,request,username):
        context = {
            "projects" : json.loads(urllib.request.urlopen('http:127.0.0.1:8000/api/projects/username='+username).read()),
        }
        return render(request,'home.html',context,username)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            profile.objects.create_user(email=email,username=username,password=password1)
            return redirect('')
        if password1 != password2:
            messages.info(request,"Passwords are not the same")
            return redirect('')
        return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        if profile.objects.filter(username=identifier):
            temp_user = profile.objects.get(username=identifier)
            user = auth.authenticate(request,email=temp_user.email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            messages.info(request,'Invalid password')
            return redirect('login')
        if profile.objects.filter(email=identifier):
            user = auth.authenticate(request,email = identifier,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            messages.info(request,'Invalid password')
            return redirect('login')
        messages.info(request,'Username/email does not exist')
        return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')