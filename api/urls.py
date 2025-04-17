

from django.contrib import admin
from django.urls import path
from .views import welcome, movie_list, review_list_create

urlpatterns = [
    path('', welcome),
    path('movies/', movie_list),
    path('movies/<int:movie_id>/reviews/', review_list_create),

]

