from django.contrib import admin
from .models import *

# Register your models here.

class animeAdmin(admin.ModelAdmin):
    list_display=("title", "date")
    prepopulated_fields={"slug": ("title",)}
  


admin.site.register(Anime, animeAdmin)
admin.site.register(Category)
