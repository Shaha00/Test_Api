from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Review, Doctor, Record
from .serializers import ReviewSerializer, DoctorSerializer, RecordSerializer
# Create your views here.


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class DoctorModelViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class RecordModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
