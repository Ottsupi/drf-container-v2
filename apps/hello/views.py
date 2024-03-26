from django.http import HttpResponse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HelloMessage
from .serializers import HelloMessageReadSerializer, HelloMessageSerializer, HelloMessageWriteSerializer


# Unused arguments should be assigned to underscore variables
def django_index(request):
    _ = request
    return HttpResponse('Hello, world!')


class DRFIndex(APIView):
    def get(self, request):
        _ = request
        return Response({'message': 'Hello, World!'})


class HelloUserView(APIView):
    def get(self, request):
        return Response({'message': f'Hello, {request.user}!'})


class HelloListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = HelloMessage.objects.all()
    serializer_class = HelloMessageSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HelloMessageWriteSerializer
        if self.request.method == 'GET':
            return HelloMessageReadSerializer
        return super().get_serializer_class()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
