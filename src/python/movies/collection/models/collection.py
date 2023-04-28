import uuid

from django.db import models
from django.contrib.auth.models import User

from .movie import Movie
class CollectionManager(models.Manager):
    '''
    Collections default manager class
    '''
    def get_all_movies(self, user):
        '''
        Return all the movies for user 
        '''
        collections_qs = self.filter(user=user)
        for collection in collections_qs:
            for movie in collection.movies.all():
                yield movie    


class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uuid = models.UUIDField()
    movies = models.ManyToManyField('Movie')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    objects = CollectionManager() 
    class Meta:
        abstract = False

    def __str__(self):
        return self.title

    def add_movie_to_collection(self,movie):
        '''
        add movie to the collection 
        '''
        assert isinstance(movie, Movie)
        assert movie is not None
        self.movies.add(movie)

    def save(self,*args,**kwargs):
        assert self.uuid is None
        assert self.title is not None and self.description is not None
        self.uuid = uuid.uuid4()
        super().save(*args,**kwargs)