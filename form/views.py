from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from .forms import *

def login(request):
    if request.user.is_authenticated():
      return redirect('index')
    else :
      loginuser=LoginForm()
      if request.method == "POST":
          loginpost = LoginForm(request.POST)
          if loginpost.is_valid():
             user = authenticate(username=loginpost.data['username'], password=loginpost.data['password'])
             if user is not None:
                 auth_login(request, user)
                 return redirect('index')
             else:
                 print("Login not OK")
                 return render (request, 'form/login.html',{'loginuser':loginuser, 'notvalidcredentials':True})
          else:
              return render (request, 'form/login.html',{'loginuser':loginuser, 'notvaliddata':True})
      return render (request, 'form/login.html',{'loginuser':loginuser})


def register(request):
    registeruser=RegisterForm()
    if request.method == "POST":
        registerpost = RegisterForm(request.POST)
        if registerpost.is_valid():
           user = User.objects.create_user(username=registerpost.cleaned_data.get('username'),
                                 email=registerpost.cleaned_data.get('email'),
                                 password=registerpost.cleaned_data.get('password'),
                                 first_name = registerpost.cleaned_data.get('first_name'),
                                 last_name = registerpost.cleaned_data.get('last_name'))
           return redirect('login')
        else:
            return render (request, 'form/register.html',{'registeruser':registeruser, 'notvaliddata':True})
    return render (request, 'form/register.html',{'registeruser':registeruser})    


def index(request):
    registeruser=RegisterSignatureForm()
    signature=SignatureForm()
    print(signature)
    if request.method == "POST":
        registerpost = RegisterSignatureForm(request.POST)
        signaturepost=SignatureForm(request.POST)
        if registerpost.is_valid() and signaturepost.is_valid():
          signature = form.cleaned_data.get('signature')
          if signature:
            signature_picture = draw_signature(signature)
            user = User.objects.create_user(username=registerpost.cleaned_data.get('email'),
                                 email=registerpost.cleaned_data.get('email'),
                                 first_name = registerpost.cleaned_data.get('first_name'),
                                 last_name = registerpost.cleaned_data.get('last_name'))
            user.signature = signature_picture
           # user = User.objects.create_user(username=registerpost.cleaned_data.get('username'),
           #                       email=registerpost.cleaned_data.get('email'),
           #                       password=registerpost.cleaned_data.get('password'),
           #                       first_name = registerpost.cleaned_data.get('first_name'),
           #                       last_name = registerpost.cleaned_data.get('last_name'))
            return redirect('index')
        else:
            return render (request, 'form/registersignature.html',{'registeruser':registeruser,'signature':signature, 'notvaliddata':True})
    return render (request, 'form/registersignature.html',{'registeruser':registeruser,'signature':signature})  









