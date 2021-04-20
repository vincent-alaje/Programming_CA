from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  #here widget is used to set the password form of input
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name', 'email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        #widget handles the rendering of the HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})}
        #Django authentication framework provides a form named UserCreationForm (which inherits from ModelForm class) to handle the creation of new users. It has three fields namely username, password1 and password2 
class LoginForm(AuthenticationForm): #authentication form make from apa so there is no work of model
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus' : True,'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False,widget= forms.PasswordInput(attrs={'autocomplete' : 'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'}) }
