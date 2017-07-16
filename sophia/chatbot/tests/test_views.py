from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class TestSpotifyBotView(TestCase):

    def setUp(self):
        self.url = reverse('chatbot:sophia')
        self.client = Client()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Error, invalid token')