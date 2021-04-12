#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path, include
from messenger.views import MessageViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'list', MessageViewSet)

urlpatterns = router.urls
