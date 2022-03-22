from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Mailing, MailingClient, Message
from .serializer import MailingSerializers, MailingClientSerializers, MessageSerializers
from datetime import datetime
from django.conf import settings
import requests


class APIMailingViewSet(ModelViewSet):
    """создание, обновление, удаление рассылки"""
    queryset = Mailing.object.all()
    serializer_class = MailingSerializers


class APIMailingClientViewSet(ModelViewSet):
    """создание, обновление, удаление клиента"""
    queryset = MailingClient.object.all()
    serializer_class = MailingClientSerializers


class APIMessageViewSet(ModelViewSet):
    """создание, обновление, удаление сообщения"""
    queryset = Message.object.all()
    serializer_class = MessageSerializers


def send_message():
    if Mailing.mailing_date > datetime.now < Mailing.stop_mailing_message:
        for client in MailingClient.objects.filter(client_tag='active'):
            url = 'https://probe.fbrq.cloud/v1/send/'
            headers = {"id": Message.message_id.objects,
                       "phone": MailingClient.client_phone,
                       "text": Mailing.mailing_message}
            response = requests.post(url=url, headers=headers)
