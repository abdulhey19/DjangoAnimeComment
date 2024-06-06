from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=30, null=False)

    def __str__(self) :
        return self.name


class Anime(models.Model):
    title=models.CharField(max_length=100, unique=True, editable=True, null=False)
    story=RichTextField()
    image_cover = models.ImageField(upload_to="movies")
    date = models.DateField(auto_created=True, auto_now=True)
    slug = models.SlugField(unique=True,db_index=True, blank=True, null=False)
    category=models.ManyToManyField(Category)
    favorite=models.ManyToManyField(User, blank=True)

    def save(self, *args, **kwargs):

        self.slug=slugify(self.title)
        super().save()
    
    def __str__(self):
        return self.title

