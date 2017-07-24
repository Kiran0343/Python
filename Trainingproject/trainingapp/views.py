# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from trainingapp.forms import userform
from django.shortcuts import render,render_to_response
from trainingapp.models import users
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from trainingapp.forms import loginform


# Create your views here.



def index(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name",'')
        last_name = request.POST.get("last_name",'')
        user_name = request.POST.get("user_name",'')
        Email = request.POST.get("Email",'')
        password = request.POST.get("password",'')
        new = users(first_name = first_name,last_name=last_name,user_name=user_name,Email=Email,password= password)
        new.save()
        return render(request,'signin.html')
    else:
        form = userform()

    return render(request,'signup.html',{'form':form,})

def index1(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        all_users = users.objects.all()
        for user in all_users:
            if (username == user.user_name and password == user.password):
                return render(request, 'welcome.html', {'name': username})
        else:
            return render(request, 'signin.html')

    return render(request, 'signin.html')


def home(request):
    all_users = users.objects.all()
    cards = {
        'all_users':all_users,
    }
    return render(request,"home.html",cards)

@login_required
def welcome(request):
    if request.method == 'POST':
        all_users = users.objects.all()
        cards = {
            'all_users': all_users,
        }
        return render(request, "welcome.html", cards)