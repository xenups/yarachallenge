from django.contrib import admin

from challenge.models import Books, Movies, Profile, Post

admin.site.register(Books)
admin.site.register(Movies)
admin.site.register(Profile)
admin.site.register(Post)
