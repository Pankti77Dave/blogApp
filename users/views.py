from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import UserLogin, UserRegister
from .models import BlogUser
from django.views.generic import CreateView, TemplateView

class BlogRegister(CreateView):
    model = BlogUser
    template_name = 'registration/register.html'
    form_class = UserRegister
    fields = '__all__'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            ue=form.cleaned_data['uname']
            up=form.cleaned_data['upassword']
            cup= request.POST.get('cupassword')
            message = ''
            if up == cup:
                add=BlogUser(uname=ue, upassword=up) 
                add.save()
                message = 'user registered successfully'   
            else:
                message = 'passwords do not match'
            return render(request, self.template_name, {'form': form, 'msg': message})   

        return render(request, self.template_name, {'form': form})

class BlogLogin(CreateView):
    model = BlogUser
    template_name = 'registration/login.html'
    form_class = UserLogin
    fields = '__all__'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            ue=form.cleaned_data['uname']
            up=form.cleaned_data['upassword']
            login=BlogUser.objects.filter(uname=ue,upassword=up)
            print(f"\n\n\n\n{login.count()}")
            if not login.count() == 0 :          
                request.session['uname'] = login[0].uname 
                return HttpResponseRedirect("/")     

        return render(request, self.template_name, {'form': form})



# def login(request):
    
#     login_form = UserLogin()
#     if request.method=="POST":
        
#         udata=UserLogin(request.POST)
#         if udata.is_valid():
#             #  to insert all data to db
#             # sdata.save()
#             # particular data to db
#             ue=udata.cleaned_data['uname']
#             up=udata.cleaned_data['upassword']
#             login=BlogUser.objects.filter(uname=ue,upassword=up)
#             print(f"\n\n\n\n{login.count()}")
#             if not login.count() == 0 :
               
#                 request.session['uname'] = login[0].uname 
#                 return HttpResponseRedirect("/")              
            
                
            
#     login_form = UserLogin()
#     # logging.debug(login_form)
#     return render(request, 'registration/login.html', {'form': login_form})
class BlogLogout(TemplateView):
    def get(self, request, *args, **kwargs):
        if 'uname' in request.session:
            del request.session['uname']
            return HttpResponseRedirect("/")