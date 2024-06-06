from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name='loginUser'),
    path('register', views.registerUser, name='registerUser'),
    path('logout', views.logoutUser, name='logoutUser'),
    path('changepass', views.changePassword, name='changePassword'),
    path('deleteuser', views.deleteUser, name='deleteUser'),
    path('favorites', views.getFavoritesAllAnimes, name='getFavoritesAllAnimes'),
    path('profile',views.showProfile, name='showProfile'),
    path('profileupdate', views.profileUpdate, name='profileUpdate'),
    path('comments', views.getUserAllComments, name='getUserAllComments'),
]