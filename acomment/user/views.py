from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RregisterForm, ChangePasswordForm,UserUpdateInfoForm
from django.contrib.auth.models import User,AnonymousUser
from django.contrib import messages
from anime.models import Anime
from comment.models import Comment



# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request,"zaten loginsin")
        return redirect("index")
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return redirect("index")
        else:
            form=LoginForm()
            return render(request, 'user/login.html',context={
                "form": form
            })
    else:
        form=LoginForm()
        return render(request, 'user/login.html',context={
            "form": form
        })


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,"zaten loginsin")
        return redirect("index")
    if request.method=="POST":
        form=RregisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            email=form.cleaned_data["email"]
            user=User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            return redirect("loginUser")
        else:
            form=RregisterForm()
            return render(request, 'user/register.html', context={
                "form": form
            })
    else:
        form=RregisterForm()
        return render(request, 'user/register.html', context={
            "form": form
        })

@login_required(login_url="/user/login")
def logoutUser(request):
    
    logout(request)
    return redirect("index")

@login_required(login_url="/user/login")
def changePassword(request):
    if request.method == "POST":
        form=ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            print("2")
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request,"parola değiştirildi.")
            return redirect("index")
        else:
            print("3")
            messages.error(request,"parola değiştirilemedi.")
            return render(request, 'user/changePass.html', context={'form': form})
            
    else:
        form=ChangePasswordForm(request.user)
        return render(request, 'user/changePass.html', context={'form': form})

@login_required(login_url="/user/login")
def deleteUser(request):
    user = request.user
    if not isinstance(user, AnonymousUser):
        if request.method == "POST":
            logout(request)
            user.delete()
            return redirect('index')  

    return render(request, 'user/deleteUser.html', {'user': user})

@login_required(login_url="/user/login")
def profileUpdate(request):
    if request.method =='POST':
        form=UserUpdateInfoForm(request.POST)
        if form.is_valid():
            user=request.user
            user.username = form.cleaned_data['username'] if form.cleaned_data['username'] != "" else user.username
            user.first_name=form.cleaned_data['first_name'] if form.cleaned_data['first_name'] != "" else user.first_name
            user.last_name=form.cleaned_data['last_name'] if form.cleaned_data['last_name'] != "" else user.last_name
            user.email=form.cleaned_data['email'] if form.cleaned_data['email'] != "" else user.email
            user.save()
            return redirect('showProfile')
        else:
            form=UserUpdateInfoForm()
            return render(request, 'user/profileupdate.html',context={'form':form})
    else:
        form=UserUpdateInfoForm()
        return render(request, 'user/profileupdate.html',context={'form':form})
        


@login_required(login_url="/user/login")
def showProfile(request):
    user=request.user
    return render(request, 'user/profile.html', context={'user':user})



@login_required(login_url="/anime")
def getFavoritesAllAnimes(request):
    user=request.user
    favorites=Anime.objects.filter(favorite=user)
    return render(request, 'user/favorites.html', context={'animes':favorites})

@login_required(login_url="/anime")
def getUserAllComments(request):
    user=request.user
    comments=Comment.objects.filter(username__id=user.id)

    return render(request, 'user/comments.html', context={'comments':comments})

    
