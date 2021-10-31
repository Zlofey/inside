from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Message
from api.serializers import MessageSerializer


class MessageView(APIView):
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        text = request.data['text'].split()
        if len(text) == 2:
            if text[0] == 'history':
                try:
                    limit = int(text[1])
                    if 1 <= limit <= 15:
                        messages = Message.objects.filter(user=self.request.user).order_by('-created_at')[:limit+1]
                        serializer = MessageSerializer(messages, many=True)
                        return Response(serializer.data)
                    else:
                        return Response("Please enter number (1 <= n <= 15) to get your latest n messages ")
                except:
                    return Response("Please enter number (1 <= n <= 15) to get your latest n messages ")

        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
