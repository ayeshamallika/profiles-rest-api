from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets


class HellopApiView(APIView):
    """Test API views"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return list of APIView Feature"""
        an_apiview = [
            'Uses HTTp methods as get, post, patch, put, delete',
            'Is similer to traditional Django View',
            'Gives most control over you application logic',
            'Is mapped  manually to urls',
        ]
        return Response({'message':'Hello','an_apiview':'an_api'})

    def post(self,request):
        "create hello and message with our name"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return response(serializer.error,status =status.HTTP_400_BAD_REQUESR)

    def put(self,request,pk=None):
        "Handle updating object"
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        "Handle partial updating object"
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        "Delete updating object"
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    "Test API  Viewset"
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        "Return a hello message"
        a_viewset = [
            'Uses actions (list,create,retrive,update,partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})

    def create(self, request):
        "create a new hello message"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =   f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.error,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request,pk=None):
        "Handle getting an object by its ID"
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        "handling updating an object"
        return Response({'http_method': 'PUT'})

    def partial_update(self,request, pk=None):
        "handling updating part of object"
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        "handle destroying object"
        return Response({'http_method': 'DELETE'})
