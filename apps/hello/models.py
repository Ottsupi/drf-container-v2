from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class HelloMessage(models.Model):
    class Channels(models.TextChoices):
        CARRIER_PIGEON = 'PIGEON', _('Carrier Pigeon')
        SNAIL_MAIL = 'SNAIL', _('Snail Mail')
        VIDEO_CALL = 'VIDEO', _('Video Call')
        VOICE_MESSAGE = 'VOICE', _('Voice Message')

    channel = models.CharField(
        max_length=6,
        choices=Channels.choices,
    )

    message = models.CharField(max_length=255)

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_messages',
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.message}" via {self.channel}'
