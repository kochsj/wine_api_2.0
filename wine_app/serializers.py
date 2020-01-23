from rest_framework import serializers
from .models import Bottle

class BottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = [
            'id', 'author', 'winery', 'grape', 'year', 'description', 'updated_at'
        ]