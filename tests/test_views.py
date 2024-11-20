from rest_framework import viewsets
from rest_framework.response import Response

class TestViewSet(viewsets.ViewSet):
    """
    Test ViewSet for API usage tracking tests
    """
    def list(self, request):
        return Response({'message': 'test'})
    
    def create(self, request):
        return Response({'message': 'created'})
    
    def retrieve(self, request, pk=None):
        return Response({'message': f'retrieved {pk}'})
