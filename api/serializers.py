from rest_framework import serializers

from api.models import Message


class MessageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']
