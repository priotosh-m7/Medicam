
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import os
import smtplib
from email.mime.text import MIMEText


def createSuperUser(request):
    admin = os.system("python manage.py createsuperuser")
    return
def index(request):
    return render(request,'index.html')

def info(request):
    return render(request,"knowledge.html")

def formsubmit(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    body = "Good Morning, " \
           "My first Mail program from python" \
           "\n\t\t\tRegards..."\
            +str(name)\
            +str(phone)
    msg = MIMEText(body)
    fromaddr = "thecapitalistbonglxix@gmail.com"
    toaddr = "priotosh.mondal7@gmail.com"
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['subject'] = "HI Friend"
    username = 'thecapitalistbonglxix@gmail.com'
    password = 'jdrxrakdvdujwhpm'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)

    server.quit()
    return redirect('home')