from rest_framework import serializers, viewsets
from .models import BookStoreModel

class BookSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model = BookStoreModel
        fields = '__all__'




