#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from rest_framework import serializers
from messenger.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Message
        read_only_fields = ('author', 'create_date', 'update_date')
        fields = '__all__'
