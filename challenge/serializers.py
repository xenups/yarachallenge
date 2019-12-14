from rest_framework import serializers
from challenge import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movies
        fields = ('id', 'title', 'director')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = ('id', 'title', 'author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    movies = MovieSerializer(many=True)
    profile = ProfileSerializer(many=False)

    class Meta:
        model = models.Post
        fields = ('books', 'movies', 'profile',)

    def create(self, validated_data):
        books_data = validated_data.pop('books')
        movies_data = validated_data.pop('movies')
        profile_data = validated_data.pop('profile')
        post = models.Post.objects.create(**validated_data)
        profile = ProfileSerializer.create(ProfileSerializer(), validated_data=profile_data)
        post.profile = profile
        for book in books_data:
            book, created = models.Books.objects.get_or_create(title=book['title'], author=book['author'])
            post.books.add(book)
        for movie in movies_data:
            movie, created = models.Movies.objects.get_or_create(title=movie['title'], director=movie['director'])
            post.movies.add(movie)
        post.save()
        return post
