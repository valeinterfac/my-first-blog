from django.contrib import admin
from .models import Post

#Import the Post model to admin page
admin.site.register(Post)
