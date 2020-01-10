from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from likes.api.mixins import LikedMixin
from ..models import TopHeadline
from .serializers import TopHeadlineSerializer


class TopHeadlineViewSet(LikedMixin,
                   viewsets.ModelViewSet):
    queryset = TopHeadline.objects.all()
    serializer_class = TopHeadlineSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
