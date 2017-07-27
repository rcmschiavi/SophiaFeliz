from django.conf.urls import url, include
from django.contrib import admin
from .views import SpotifyBotView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^chatbot/?$', SpotifyBotView.as_view(), name='chatbot'),
]
