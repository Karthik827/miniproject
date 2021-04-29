from django.contrib import admin
from moviesApp.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['date','moviename','hero','heroine','rating']

admin.site.register(Movie,MovieAdmin)