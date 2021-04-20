from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import SignUpForm,LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
# import datetime

  # django provide defaut form
# for home page view
def home(request):
    posts=Post.objects.all()
    return render(request,'Digital_Diary_app/home.html',{'posts':posts})
    # for about page view
def about(request):
    return render(request,'Digital_Diary_app/about.html')
        # for about page view
def contact(request):
    return render(request,'Digital_Diary_app/contact.html')
        # for dashboard page view
def dashboard(request):
    if request.user.is_authenticated: # if user is loggedin then the dashboard page will show 
        posts=Post.objects.filter(user=request.user) #current user post
        user=request.user
        full_name = user.get_full_name()
        gps=user.groups.all()
        return render(request,'Digital_Diary_app/dashboard.html',{'posts':posts , 'full_name':full_name , 'groups':gps})
        
    else:
        return HttpResponseRedirect('/user_login/') #otherwise first user should be login after that user can access dashboard 
        # for logout page view
def search(request):

    query = request.GET['query']
    posts=Post.objects.filter(title__icontains=query)
    
    params={'posts':posts}
    return render(request,'Digital_Diary_app/search.html',params)
   
       
    '''if request.user.is_authenticated: # if user is loggedin then the dashboard page will show 
        if 'q' in request.GET:
            q=request.GET['q']
            posts=Post.objects.filter(title_icontains=q) #current user post
            user=request.user
            full_name = user.get_full_name()
            gps=user.groups.all()
            return render(request,'Digital_Diary_app/search.html',{'posts':posts , 'full_name':full_name , 'groups':gps})
       '''
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
        # for signup page view
def user_signup(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!! You have become a part of Writing Room')
            user=form.save()
            group=Group.objects.get(name='Writer')       #to assign user in group
            user.groups.add(group)  #to add the group
    else:
        form=SignUpForm()
    return render(request,'Digital_Diary_app/signup.html',{'form':form})
    
        # for Login page view
def user_login(request):
    if not request.user.is_authenticated: # if user is not logged in then it will show the 
        if request.method=="POST":
            form= LoginForm(request=request,data=request.POST)
            if form.is_valid(): #check validation then store the data for authentication
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                #for authenticate or check and match the data with stored data
                user= authenticate(username= uname,password=upass) #after successfully verification of username and password we get object as user
                if user is not None:
                    login(request,user)
                    
                    return HttpResponseRedirect('/dashboard/')
        else: # if data is t valid or matchd then it will return blank login form
            form=LoginForm()
        return render(request,'Digital_Diary_app/login.html',{'form':form})
            
    else: # means already logged in then it will return or how the dashboard to the user
        return HttpResponseRedirect('/dashboard/')




    
# to add new post
def addPost(request):
    if request.user.is_authenticated:
        if request.method=='POST':  
            form= PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc=  form.cleaned_data['desc']
                #date = form.cleaned_data['date']
                #created_at=form.cleaned_data['created_at']
                #updated_at=form.cleaned_data['updated_at']
                pst = Post(title=title,desc=desc,user=request.user)
                pst.save()
                
                return redirect('/dashboard/')
                # form=PostForm()

        else:
            form=PostForm()
        return render(request,'Digital_Diary_app/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/user_login/')
# to update posted info
def updatePost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return redirect('/dashboard/')
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'Digital_Diary_app/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/user_login/')
# to delete the posted info
def deletePost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/user_login/')

def carousel(request):
    return render(request,"carousel.html")
'''
def search(request):
    return HttpResponseRedirect('This is search')
'''
class PasswordResetView(TemplateView):
    template_name = "password_reset.html"    

class PasswordResetDoneView(TemplateView):
    template_name = "password_reset_done.html"    

class PasswordResetConfirmView(TemplateView):
    template_name = "password_reset_confirm.html"
  