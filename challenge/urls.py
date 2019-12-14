from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from challenge import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create_uri/', views.CreateURI.as_view()),

    path('uris/<slug:slug>/movies/', views.MoviesListView.as_view()),
    path('uris/<slug:slug>/movies/<int:pk>/', views.MoviesDetailView.as_view()),

    path('uris/<slug:slug>/books/', views.BooksListView.as_view()),
    path('uris/<slug:slug>/books/<int:pk>/', views.BooksDetailView.as_view()),

    path('uris/<slug:slug>/profile/', views.ProfileView.as_view()),

]
