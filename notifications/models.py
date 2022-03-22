from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.


class Mailing(models.Model):
    mailing_id = models.AutoField()
    mailing_date = models.DateTimeField(auto_now_add=True)
    mailing_message = models.CharField(max_length=100)
    mailing_tag = TaggableManager()
    stop_mailing_message = models.DateTimeField(auto_now_add=True)


class MailingClient(models.Model):
    client_id = models.AutoField()
    client_phone = models.IntegerField()
    phone_cod = models.IntegerField()
    client_tag = TaggableManager()
    client_timezone = settings.TIME_ZONE


class Message(models.Model):
    message_id = models.AutoField()
    message_date = models.DateTimeField(auto_now=True)
    message_status = TaggableManager()
    mailing_id_message = models.OneToOneField(Mailing, on_delete=models.CASCADE)
    client_id_message = models.ForeignKey(MailingClient, on_delete=models.CASCADE)

