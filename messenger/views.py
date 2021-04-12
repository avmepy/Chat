from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from messenger.models import Message
from messenger.serializers import MessageSerializer
from django.utils import timezone


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):

        message_data = self.request.data
        print(message_data, self.request.user.is_anonymous, timezone.now())
        cur_author = self.request.user
        if cur_author.is_anonymous:
            cur_author = None

        new_message = Message.objects.create(author=cur_author,
                                             email=message_data['email'],
                                             text=message_data['text'],
                                             create_date=timezone.now(),
                                             update_date=timezone.now())
        new_message.save()
        serializer = MessageSerializer(new_message)
        return Response(serializer.data)
