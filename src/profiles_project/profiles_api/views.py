from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test Api View."""

    def get(self,request,format=None):
        """Returns a list of APIView features."""
        
        an_apiview = ['Uses Http methods as function (get,psot,patch,put,delte)',
                        'It is simliar to a traditional Django view',
                        'Gives you the most control over your logic'
                        ]
        return Response({'message':'Hello!','an_apiview': an_apiview})
    

