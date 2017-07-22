import json
from pprint import pprint

from django.conf import settings
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .Respostas import operacao
from .Respostas import respauto
from .utils import post_facebook_message
from operacoes.Manager_DB import  select_info_user_db
from .mensagens import post_ola

class SpotifyBotView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == settings.TOKEN_2:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))


        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    pprint(message)
                    #operacao(message['sender']['id'],message['message']['text'])
                    #teste()
                    #post_ola(message['sender']['id'])
                    respauto(message['sender']['id'],message['message']['text'])
                    #post_facebook_message(message['sender']['id'],"OI")
        return HttpResponse()
