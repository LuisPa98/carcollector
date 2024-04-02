from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Shoe
from.serializers import ShoeSerializer

# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the shoe-collector api home route!'}
        return Response(content)

class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    lookup_field = 'id'