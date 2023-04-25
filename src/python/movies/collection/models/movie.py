from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uuid = models.UUIDField(unique=True)
    genres = models.CharField(max_length=100)

    def __str__(self):
        return self.title