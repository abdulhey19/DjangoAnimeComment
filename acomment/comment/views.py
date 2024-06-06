from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required
from anime.models import Anime
from .models import Comment,Likes
from django.contrib.auth.models import User
from .forms import CommentForm

# Create your views here.

@login_required(login_url="/user/login")
def addComment(request,slug):
    user=request.user
    anime=Anime.objects.get(slug=slug)
    if not isinstance(user, AnonymousUser): 
        if request.method=='POST':
            description=request.POST.get('comment')
            description=description.strip()
            comment=Comment.objects.create(description=description, username=user, anime=anime)
            comment.save()
            return redirect(reverse("getAnime", args=(slug,)))
    
    return redirect(reverse("getAnime", args=(slug,)))
    

def addOrDeleteLike(request,id):
    
    comment=Comment.objects.get(id=id)
    likes=Likes.objects.filter(comment=comment)
    anime=Anime.objects.get(id=comment.anime_id)
    user = request.user
  
    if not isinstance(user, AnonymousUser):    
        userCount=Likes.objects.filter(comment=comment , username=user).count() 
        if userCount > 0:
            for like in likes:
                if like.username==user:
                    if like.nDisliked == False:
                        if like.nLike:
                            like.delete()
                            comment.nLike -=1
                            comment.save()
                            
                            break
        else:
            like=Likes.objects.create(username=user,comment=comment,nLike=True, nDisliked=False)
            like.save()
            comment.nLike += 1
            comment.save()
            
    else:
        like=Likes.objects.create(comment=comment,nLike=True, nDisliked=False)
        like.save()
        comment.nLike += 1
        comment.save() 
                       
    return redirect(reverse("getAnime", args=(anime.slug,)))


def addOrDeleteDisLike(request,id):
    
    comment=Comment.objects.get(id=id)
    likes=Likes.objects.filter(comment=comment)
    anime=Anime.objects.get(id=comment.anime_id)
    user = request.user
    control=True
    
    if not isinstance(user, AnonymousUser):  
        userCount=Likes.objects.filter(comment=comment, username=user).count()
        if userCount > 0:
            for like in likes:
                if like.username==user:
                    if like.nLike == False:    
                        if like.nDisliked:
                            like.delete()
                            comment.nDislike -=1
                            comment.save()
                            control=False
                            break
        else:
            dislike=Likes.objects.create(username=user,comment=comment,nLike=False, nDisliked=True)
            dislike.save()
            comment.nDislike += 1
            comment.save()   
    else:
        dislike=Likes.objects.create(comment=comment,nLike=False, nDisliked=True)
        dislike.save()
        comment.nDislike += 1
        comment.save()
      
    return redirect(reverse("getAnime", args=(anime.slug,)))

@login_required(login_url="/user/login")
def deleteOneComment(request,id):
    user=request.user
    comment=get_object_or_404(Comment, id=id)

    if not isinstance(user, AnonymousUser):
        if user.id == comment.username_id:
            comment.delete()

            return redirect("index")
        else:
            return redirect("index")


@login_required(login_url="/user/login")
def updateOneComment(request,id):
    user=request.user
    comment=get_object_or_404(Comment, id=id)

    if not isinstance(user, AnonymousUser) and user.id == comment.username_id:
        form=CommentForm(request.POST or None,instance=comment)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.description=request.POST.get("description").strip()
            comment.save()
            return redirect("index")
        return render(request, "comment/updateComment.html", {"form": form})

