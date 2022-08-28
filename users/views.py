from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserLogin, UserRegister
from .models import BlogUser

def register(request):
    register_form = UserRegister()
    if request.method=="POST":
        
        udata=UserRegister(request.POST)
        if udata.is_valid():
            #  to insert all data to db
            # sdata.save()
            # particular data to db

            ue=udata.cleaned_data['uname']
            up=udata.cleaned_data['upassword']
            cup= request.POST.get('cupassword')
            message = ''
            if up == cup:
                add=BlogUser(uname=ue, upassword=up) 
                add.save()
                message = 'user registered successfully'   
            else:
                message = 'passwords do not match'
            return render(request, 'registration/register.html', {'form': register_form, 'msg': message})    
                
            
    return render(request, 'registration/register.html', {'form': register_form})    

def login(request):
    
    login_form = UserLogin()
    if request.method=="POST":
        
        udata=UserLogin(request.POST)
        if udata.is_valid():
            #  to insert all data to db
            # sdata.save()
            # particular data to db
            ue=udata.cleaned_data['uname']
            up=udata.cleaned_data['upassword']
            login=BlogUser.objects.filter(uname=ue,upassword=up)
            print(f"\n\n\n\n{login.count()}")
            if not login.count() == 0 :
               
                request.session['uname'] = login[0].uname 
                return HttpResponseRedirect("/")              
            
                
            
    login_form = UserLogin()
    # logging.debug(login_form)
    return render(request, 'registration/login.html', {'form': login_form})

def logout(request):
    if 'uname' in request.session:
        del request.session['uname']
        return HttpResponseRedirect("/")