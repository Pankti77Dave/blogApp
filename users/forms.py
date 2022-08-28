from .models import BlogUser
from django import forms

class UserLogin(forms.ModelForm):
    class Meta:
        model= BlogUser
        fields =['uname','upassword']
        widgets={
            'uname':forms.TextInput(attrs={'class':'form-control'}),
            'upassword':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }