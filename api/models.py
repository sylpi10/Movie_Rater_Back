from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=360)

    def nb_of_ratings(self):
        # select all ratings for current movie
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        # select all ratings for current movie
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
            if len(ratings) > 0:
                return sum/len(ratings)
            else:
                return 0

    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
