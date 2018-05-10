from django.urls import path

from search import views

urlpatterns = [
    path('', views.get_search_player, name='get-search-player'),
]
