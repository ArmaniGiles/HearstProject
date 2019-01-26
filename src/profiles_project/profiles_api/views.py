from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
# Create your views here.
from . import serializers


class HelloApiView(APIView):
    """Test Api View."""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features."""
        
        an_apiview = ['Uses Http methods as function (get,psot,patch,put,delte)',
                        'It is simliar to a traditional Django view',
                        'Gives you the most control over your logic'
                        ]
        return Response({'message':'Hello!','an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)
        print("request.data : ",request.data)
        print("serializers.HelloSerializer(data=request.data) : ",serializers.HelloSerializer(data=request.data))

        if serializer.is_valid():
            name = serializer.data.get('name')
            print("serializer.data.get('name') : ",serializer.data.get('name'))
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method' :'patch'})

    def delete(self,request, pk=None):
        """Deletes and object."""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test APi viewSet."""
    def list(self, request):
        """Return a hello message."""
        a_viewset =['Uses actions (list,create,retrieve,update, partial_update)',
        "Automatically maps to URLS using Routers",
        "Provides more functionality with less code."
        ]

        return Response({'message' :'Hello!','a_viewset':a_viewset})
        

