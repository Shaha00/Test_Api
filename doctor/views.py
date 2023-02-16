from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Review
from .serializers import ReviewSerializer
# Create your views here.


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'