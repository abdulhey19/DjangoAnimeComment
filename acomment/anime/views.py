from django.shortcuts import render,redirect, get_object_or_404
from django.db.models import Count
from .models import Anime, Category
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.forms import Form
from comment.models import Comment,Likes
from comment.forms import CommentForm

# Create your views here.
def index(request):
    animes=Anime.objects.all()
    return render(request, 'anime/index.html', context={
        'animes': animes
    })


def getAnime(request, slug):
    anime=Anime.objects.get(slug=slug)
    categories=Category.objects.filter(anime__id=anime.id)
    comments=Comment.objects.filter(anime__id=anime.id)
    user=request.user 
    
    """ 
        if koşulu animenin login olan kullanıcının favorilerinin de kayıtlı olup olmadığını kontrol ediyor...
        kayıtlı ise favorite objesi içinde gönderiyor...
    
    """
    if not isinstance(user, AnonymousUser): 
        likes=[]
        for comment in comments:
            like=Likes.objects.filter(comment=comment, username=user)
            likes.append(like)

        favorite=Anime.objects.filter(favorite=user) 
        if anime in favorite:
            return render(request, "anime/anime_details.html",context={
            'anime': anime,
            'categories': categories,
            'favorite':favorite,
            'comments':comments,
            'likes':likes,
            'user':user
        }) 
    
        return render(request, "anime/anime_details.html",context={
            'anime': anime,
            'categories': categories,
            'comments':comments,
            'likes':likes
        })

    return render(request, "anime/anime_details.html",context={
        'anime': anime,
        'categories': categories,
        'comments':comments
    })


def getAllCategories(request):
    categories=Category.objects.all()
    filmSayisi=[]

    for category in categories:
        sayi=Anime.objects.filter(category__id=category.id).count()
        filmSayisi.append({"name": category.name,
                           "sayi": sayi})
   
    return render(request, 'anime/kategoriler.html', context={'categories': categories, 'sayi':filmSayisi})


def oneCategory(request, id):
    animes=Anime.objects.filter(category__id=id)
    category=Category.objects.get(id=id)
    return render(request, "anime/kategori.html", context={'animes':animes, 'category':category})


def addOrDeleteFavorites(request, slug):
    user=request.user
    if not isinstance(user, AnonymousUser): 
        anime=Anime.objects.get(slug=slug)
       
        if anime.favorite.filter(id=user.id).exists():
            anime.favorite.remove(user)
        else:
            anime.favorite.add(user)  
        return redirect(reverse('getAnime', args=(slug,)))
    else:
        return redirect('loginUser')


def top10AnimeList(request):
    
    top10Anime = Anime.objects.annotate(favorite_count=Count('favorite')).order_by('-favorite_count')[:10]
    return render(request, 'anime/top10.html', {'animes': top10Anime})



def showSearchResults(request):
    form=Form(request.POST or None )
    if form.is_valid():
        metin=request.POST.get('search')
        animeList=Anime.objects.all()
        resultList=[]
        try:
            for anime in animeList:
                if anime.title.lower().rfind(metin.lower())!= -1:
                    resultList.append(anime)
        except:
            resultList=[]

        return render(request, 'anime/searchResult.html', {'animes': resultList})   

        
    return redirect("index")