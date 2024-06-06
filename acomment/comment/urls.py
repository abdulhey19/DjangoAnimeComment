from django.urls import path
from . import views 

urlpatterns = [
    path('addcomment/<slug:slug>', views.addComment,name="addComment"),
    path('addOrDeleteLike/<int:id>', views.addOrDeleteLike,name="addOrDeleteLike"),
    path('addOrDeleteDisLike/<int:id>', views.addOrDeleteDisLike,name="addOrDeleteDisLike"),
    path('delete/<int:id>', views.deleteOneComment,name="deleteOneComment"),
    path('update/<int:id>', views.updateOneComment,name="updateOneComment"),
]