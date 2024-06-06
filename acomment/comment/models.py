from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from anime.models import Anime


# Create your models here.

class Comment(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    anime=models.ForeignKey(Anime, on_delete=models.CASCADE)
    description=RichTextField()
    date=models.DateField(auto_now_add=True)
    nLike=models.IntegerField(default=0, null=True)
    nDislike=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.nLike + "  // " + self.nDislike 

class Likes(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nLike=models.BooleanField(default=False)
    nDisliked=models.BooleanField(default=False)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}-{self.nLike}-{self.nDisliked} "


    
