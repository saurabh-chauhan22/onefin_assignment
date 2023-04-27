from django.db import models

class MovieManager(models.Manager):
    pass

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uuid = models.UUIDField(unique=True)
    genre = models.CharField(max_length=100)

    objects = MovieManager()
    class Meta:
        abstract = False

    def __str__(self):
        return self.title
    
    def add_movie(self, title, description, uuid, genre):
        movie, created = Movie.objects.get_or_create(title=title,description=description,uuid=uuid,genre=genre)
        movie.save()
        return movie

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)