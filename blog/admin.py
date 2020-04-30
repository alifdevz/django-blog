from django.contrib import admin
from blog.models import Post, Publisher, Genre

# Register your models here.
admin.site.register(Post)
admin.site.register(Publisher)
admin.site.register(Genre)