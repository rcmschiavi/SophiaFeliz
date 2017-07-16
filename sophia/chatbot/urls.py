from django.conf.urls import include, url
from .views import SpotifyBotView

urlpatterns = [
    url('^sophia/?$', SpotifyBotView.as_view(), name='sophia')
]