from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('favorite/<slug:slug>',views.addOrDeleteFavorites, name="addOrDeleteFavorites"),
    path('top10', views.top10AnimeList, name="top10AnimeList"),
    path('kategoriler', views.getAllCategories, name="getAllCategories"),
    path('kategori/<int:id>', views.oneCategory, name="oneCategory"),
    path("search/", views.showSearchResults, name="showSearchResults"),
    path('<slug:slug>', views.getAnime, name="getAnime"),
]