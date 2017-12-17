from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.views import Response


# Create your views here.

class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format = None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patc, put, delete)',
            'It is similar to a tranditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message' : 'Hello', 'an_apiview': an_apiview})
