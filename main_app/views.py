from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Shoe, Worn, Shoelace
from.serializers import ShoeSerializer, WornSerializer, ShoelaceSerializer

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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        shoelaces_not_associated = Shoelace.objects.exclude(id__in=instance.shoelace.all())
        shoelaces_serializer = ShoelaceSerializer(shoelaces_not_associated, many=True)

        return Response({
            'shoe': serializer.data,
            'shoelaces_not_associated': shoelaces_serializer.data
        })

class WornListCreate(generics.ListCreateAPIView):
    serializer_class = WornSerializer

    def get_queryset(self):
        shoe_id = self.kwargs['shoe_id']
        return Worn.objects.felter(shoe_id=shoe_id)

    def perform_create(self, serializer):
        shoe_id = self.kwargs['shoe_id']
        shoe = Shoe.object.get(id=shoe_id)
        serializer.save(shoe=shoe)

class WornDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WornSerializer
    lookup_field = 'id'

    def get_queryset(self):
        shoe_id = self.kwargs['shoe_id']
        return Worn.objects.filter(shoe_id=shoe_id)

class ShoelaceList(generics.ListCreateAPIView):
    queryset = Shoelace.objects.all()
    serializer_class = ShoelaceSerializer

class ShoelaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoelace.objects.all()
    serializer_class = ShoelaceSerializer
    lookup_field = 'id'

class AddShoelaceToShoe(APIView):
    def post(self, request, shoe_id, shoelace_id):
        shoe = Shoe.objects.get(id=shoe_id)
        shoelace = Shoelace.objects.get(id=shoelace_id)
        shoe.shoelaces.add(shoelace)
        return Response({'message': f'{shoelace.shoelacetype}, and {shoelace.color} Shoelaces added to Shoe {shoe.name}'})

class RemoveShoelaceFromShoe(APIView):
    def post(self, request, shoe_id, shoelace_id):
        shoe = Shoe.objects.get(id=shoe_id)
        shoelace = Shoelace.objects.get(id=shoelace_id)
        shoe.shoelace.remove(shoelace)
        return Response({'message': f'{shoelace.shoelacetype}, and {shoelace.color} Shoelaces removed from Shoe {shoe.name}'})