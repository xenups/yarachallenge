import random

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from challenge import models
from challenge import serializers
from challenge.permissions import IsOwner


class CreateURI(generics.CreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def __generate_slug():
        return ''.join(str(random.randint(0, 9)) for _ in range(8))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        generated_slug = self.__generate_slug()
        self.perform_create(serializer, generated_slug)
        headers = self.get_success_headers(serializer.data)
        return Response(({'uri': generated_slug}), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, slug):
        serializer.save(slug=slug, owner=self.request.user)


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        post = get_object_or_404(models.Post, slug=slug, owner=self.request.user)
        return post.profile


class MoviesListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.MovieSerializer

    def get_queryset(self):
        post = get_object_or_404(models.Post, slug=self.kwargs.get('slug'), owner=self.request.user)
        return post.movies.all()


class MoviesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.MovieSerializer

    def get_queryset(self):
        post = get_object_or_404(models.Post, slug=self.kwargs.get('slug'), owner=self.request.user)
        return post.movies.all()


class BooksListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        post = get_object_or_404(models.Post, slug=self.kwargs.get('slug'), owner=self.request.user)
        return post.books.all()


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        post = get_object_or_404(models.Post, slug=self.kwargs.get('slug'), owner=self.request.user)
        return post.books.all()
