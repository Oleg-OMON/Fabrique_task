from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import APIMailingViewSet, APIMailingClientViewSet, APIMessageViewSet

router_mailing = DefaultRouter
router_mailing.register('mailing', APIMailingViewSet)

router_client = DefaultRouter
router_client.register('client', APIMailingClientViewSet)

router_message = DefaultRouter
router_message.register('message', APIMailingClientViewSet)

urlpatterns = [
    path('api/', include(router_mailing.urls)),
    path('api/', include(router_client.urls)),
    path('api/', include(router_message.urls))
]
