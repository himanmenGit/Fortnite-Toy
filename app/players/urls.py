from django.urls import path

from players.views import PlayerDetailView

urlpatterns = [
    path('', PlayerDetailView.as_view(), name='player-detail'),
]
