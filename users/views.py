from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserLogin
from .models import BlogUser

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

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