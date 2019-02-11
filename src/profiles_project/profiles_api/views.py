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

from datetime import date


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
        serializer = serializers.HelloSerializer(data=request.data)# is this creating an object or refererencing a class?

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
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name', 'email',)

    def list(self, request):
        term = request.GET.get('term')
        if term:
            self.queryset = self.queryset.filter(name__istartswith=term)
        return super(UserProfileViewSet, self).list(request)

def authenticate_user(request):
    from rest_framework.authtoken.models import Token
    #Token.objects.create(user=user)
    pass

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()

    def list(self, request):
        term = request.GET.get('term')
        if term:
            self.queryset = self.queryset.filter(name__istartswith=term)
        start_date = request.GET.get('start_date')
        if start_date:
            # start_date must be in YYYY-MM-DD format
            start_date = start_date.split('-')
            year, month, day = int(start_date[0]), int(start_date[1]), int(start_date[2])
            start_date = date(year, month, day)
            self.queryset = self.queryset.filter(startDate__gte=start_date)
        return super(CourseViewSet, self).list(request)

        

