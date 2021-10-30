from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from api.serializers import MessageWriteSerializer


# class Message(ListCreateAPIView):

# class PrepaidCardView(generics.CreateAPIView):
#     serializer_class = CardCreateSerializer
#     permission_classes = [IsAdminUser]
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         card = serializer.save()
#         card.state = 'payed'
#         card.payed = timezone.now()
#         card.created_from = 'admin'
#         card.save()
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageView(CreateAPIView):
    serializer_class = MessageWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)