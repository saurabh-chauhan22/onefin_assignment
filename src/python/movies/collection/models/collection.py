from django.db import models
from django.contrib.auth.models import User

from .movie import Movie
class CollectionManager(models.Manager):
    '''
    Collections default manager class
    '''
    def get_all_movies(self):
        '''
        Return all the movies from all the collections 
        '''
        collections_qs = self.all()
        for collection in collections_qs:
            for movie in collection.movies.all():
                yield movie    


class Collection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
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

    def add_collection(self, title, description, user, movie):
        '''
        Add collection with movie and the user associated for the collection
        '''
        assert title is not None
        assert description is not None
        assert user is not None
        assert movie is not None
        
        collection = Collection(title=title, description=description, user=user)
        self.add_movie_to_collection(movie)
        collection.save()
        return collection