#rest api 
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#model
from info.models import ContentWebPage
from info.serializers import ContentWebPageSerializer


class ContentWebPageViewSet(viewsets.ModelViewSet):
    queryset = ContentWebPage.objects.all()
    serializer_class = ContentWebPageSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]




