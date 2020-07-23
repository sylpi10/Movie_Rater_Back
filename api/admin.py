from django.contrib import admin

from api.models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    # list_editable = ['title', 'description']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'stars']
    # list_editable = ['movie', 'user']