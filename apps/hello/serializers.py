from zoneinfo import ZoneInfo

from rest_framework import serializers

from .models import HelloMessage


class HelloMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessage
        fields = ('channel', 'message', 'sender', 'date_created', 'last_modified')


class HelloMessageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessage
        fields = ('channel', 'message')


class HelloMessageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloMessage
        fields = ('channel', 'message', 'sender', 'date_created', 'last_modified')

    def to_representation(self, instance: HelloMessage):
        data = super().to_representation(instance)

        # Convert UTC to Japan time
        tokyo = ZoneInfo('Asia/Tokyo')
        display_format = '%Y-%m-%d %H:%M:%S %Z'
        data['date_created'] = instance.date_created.astimezone(tokyo).strftime(display_format)
        data['last_modified'] = instance.last_modified.astimezone(tokyo).strftime(display_format)

        # Display human-readable name
        data['channel'] = instance.get_channel_display()

        return data
