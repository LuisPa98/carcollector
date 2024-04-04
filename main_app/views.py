from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Shoe, Worn, Shoelace
from.serializers import ShoeSerializer, WornSerializer, ShoelaceSerializer, UserSerializer

# Create your views here.

class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the shoe-collector api home route!'}
        return Response(content)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user: 
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(username=request.user)
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })

class ShoeList(generics.ListCreateAPIView):
    serializer_class = ShoeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Shoe.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShoeSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return Shoe.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        shoelaces_not_associated = Shoelace.objects.exclude(id__in=instance.shoelace.all())
        shoelaces_serializer = ShoelaceSerializer(shoelaces_not_associated, many=True)

        return Response({
            'shoe': serializer.data,
            'shoelaces_not_associated': shoelaces_serializer.data
        })

        def perform_update(self, serializer):
            shoe = self.get_object()
            if shoe.user != self.request.user:
                raise PermissionDenied({"message": "You do not have permission to edit this shoe."})
            serializer.save()

        def perform_destroy(self, instance):
            if instance.user != self.request.user:
                raise PermissionDenied({"message": "You do not have permission to delete this shoe."})

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