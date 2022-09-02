
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import ContentWebPage

class ContentWebPageSerializer(ModelSerializer):

    class Meta:
        model = ContentWebPage
        fields = ['id','name','language','content']