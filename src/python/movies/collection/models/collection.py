from django.db import models
from django.contrib.auth.models import User

class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    movies = models.ManyToManyField('Movie')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title