from django.contrib.messages.storage.cookie import MessageSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from .serializers import ClientSerializer, MailingSerializer
from .models import Client, Message, Mailing


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny, ]


class ClientAllCont(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny, ]


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [AllowAny, ]


class MessageAllCont(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [AllowAny, ]


class MailingList(generics.ListCreateAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    permission_classes = [AllowAny, ]


class MailingAllCont(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()
    permission_classes = [AllowAny, ]
