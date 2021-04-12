from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    email = models.CharField(verbose_name='Email', max_length=100)
    text = models.CharField(verbose_name='Message text', max_length=100)
    create_date = models.DateTimeField(verbose_name='Create date')
    update_date = models.DateTimeField(verbose_name='Update date')

    def __str__(self):
        return f'Message {self.author} {self.text[:10]}'
