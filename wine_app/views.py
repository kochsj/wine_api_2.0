from rest_framework import generics
from .models import Bottle
from .serializers import BottleSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class BottleList(generics.ListCreateAPIView):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer

class BottleListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    permission_classes = (IsAuthorOrReadOnly,)