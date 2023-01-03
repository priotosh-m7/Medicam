
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import os


def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return
def index(request):
    return render(request,'index.html')

def info(request):
    return render(request,"knowledge.html")