from rest_framework import generics
from .models import Bottle
from .serializers import BottleSerializer

# Create your views here.
class BottleList(generics.ListAPIView):
    model = Bottle
    serializer_class = BottleSerializer