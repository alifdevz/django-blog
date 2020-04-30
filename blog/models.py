from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, default=None)
    genre = models.ManyToManyField(Genre)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title