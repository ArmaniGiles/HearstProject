from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from . import models
from . import permissions
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
        print("request : ", request)
        serializer = serializers.HelloSerializer(data=request.data)
        print("request.data : ",request.data)
        print("serializers.HelloSerializer(data=request.data) : ",serializers.HelloSerializer(data=request.data))

        if serializer.is_valid():
            name = serializer.data.get('na')
            print("serializer.data.get('n') : ",serializer.data.get('na'))
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
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message."""
        a_viewset =['Uses actions (list,create,retrieve,update, partial_update)',
        "Automatically maps to URLS using Routers",
        "Provides more functionality with less code."
        ]

        return Response({'message' :'Hello!','a_viewset':a_viewset})

    def create(self, request ):
        """Create a new Hello message."""
        print("SDSDFDSFDsdf")
        print("request : ",request)

        print("request.data : ",request.data)
        serializer = serializers.HelloSerializer(data=request.data)# is this creating an object or refererencing a class?
        print("serializer : ",serializer)

        if serializer.is_valid():# is this deserializing
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request, pk=None):
        """Handles getting an object by its ID."""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handles updating part of an object"""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object """

        return Response({'http_method' : 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, amd updating profiles"""
    
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name', 'email',)
    print("serializer_class : SSSSSSSSSSS ",serializer_class)
    print("models.UserProfile.objects.all() : ",models.UserProfile.objects.all())
    #are we extracting frm the database what does it actual do?
    print("Wow")
    # print("queryset : ",queryset)
    #queryset = models.UserProfile.objects.filter(name__startswith='a')
    # what do the queryset do?
    # why is AAAAAAA is print?
    #does the ModelViewSet herit its properties from viewset
    #can you fix my script?


# class TestAPIView():

#     def get(request):
#         pass

#     def post(request):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         models.UserProfile.objects.create(name=name, email = email)
#         # return Response()
#         pass