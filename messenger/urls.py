#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path
from messenger.views import MessageListView, MessageCreateView, \
    MessageRetrieveUpdateDestroyView, MessageListViewPaginate


urlpatterns = [
    # path('list/', MessageListView.as_view(), name='messages_list'),  # pagination with url list/?page={page_num}
    path('list/<int:page>/', MessageListViewPaginate.as_view(), name='messages_list_pag'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('single/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message_single'),
]

