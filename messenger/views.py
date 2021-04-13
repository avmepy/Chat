from django.core.paginator import Paginator, EmptyPage
from rest_framework import permissions, pagination
from rest_framework import generics
from rest_framework.response import Response
from messenger.models import Message
from messenger.serializers import MessageSerializer
from django.utils import timezone
from messenger import services
from django.core.exceptions import ValidationError


class MessageListView(generics.ListAPIView):
    """
    list view
    pagination with url ^/?page={page_num}
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = pagination.PageNumberPagination


class MessageListViewPaginate(generics.ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        page_number = kwargs['page']
        paginator = Paginator(instance, 10)  # using django paginator

        # catching request with non-existent page number
        try:
            page_obj = paginator.page(page_number)
        except EmptyPage:
            return Response('That page contains no results')

        serializer = MessageSerializer(list(page_obj), many=True)
        return Response(serializer.data)


class MessageCreateView(generics.CreateAPIView):
    """
    creating new message
    """
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):

        message_data = self.request.data

        # validate mail
        if not services.valid_mail(message_data['email']):
            raise ValidationError(message='Invalid mail')

        # validate message
        if not services.valid_message(message_data['text']):
            raise ValidationError(message='Invalid message text. Msg must not be empty. Length of msg must be < 100')

        # author: user if authenticated or None (null in db)
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


class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    read-write-delete
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny, )

    def retrieve(self, request, *args, **kwargs):
        """
        get msg py pk (id)
        """
        message = self.queryset.get(id=self.kwargs['pk'])
        serializer = MessageSerializer(message)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        put method
        was not in tz
        so I only added update_date
        didn't know if it was necessary to define access rights
        """

        # similar to create method
        # except update date
        message_data = self.request.data

        if not services.valid_mail(message_data['email']):
            raise ValidationError(message='Invalid mail')

        if not services.valid_message(message_data['text']):
            raise ValidationError(message='Invalid message text. Msg must not be empty. Length of msg must be < 100')

        cur_message = Message.objects.get(id=kwargs['pk'])
        cur_message.email = message_data['email']
        cur_message.text = message_data['text']
        cur_message.update_date = timezone.now()
        cur_message.save()
        serializer = MessageSerializer(cur_message)

        return Response(serializer.data)
