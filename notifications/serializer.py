from rest_framework import serializers
from .models import Message, MailingClient, Mailing


class MailingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ('mailing_id', 'mailing_date',
                  'mailing_message', 'mailing_tag',
                  'stop_mailing_message')


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message_id', 'message_date',
                  'mailing_id_message', 'client_id_message',
                  'message_status')


class MailingClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = MailingClient
        fields = ('client_id', 'client_phone',
                  'phone_cod', 'client_tag',
                  'client_timezone')
