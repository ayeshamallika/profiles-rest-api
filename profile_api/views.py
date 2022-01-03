from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from profile_api import serializers



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
