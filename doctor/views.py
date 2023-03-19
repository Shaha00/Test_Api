from requests import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Review, Doctor, Record
from .serializers import ReviewSerializer, DoctorSerializer, RecordSerializer, DoctorValidateSerializer, DoctorDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status

# Create your views here.


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class RecordModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


class DoctorListCreateAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DoctorValidateSerializer
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        author = serializer.validated_data.get('author')
        doctor = serializer.validated_data.get('doctor')
        text = serializer.validated_data.get('text')
        created_date = serializer.validated_data.get('created_date')

        review = Review.objects.create(author=author, doctor=doctor, text=text, created_date=created_date)
        return Response(data=DoctorDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)

class DoctorDetailListCreateAPIView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = DoctorValidateSerializer
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        author = serializer.validated_data.get('author')
        doctor = serializer.validated_data.get('doctor')
        text = serializer.validated_data.get('text')
        created_date = serializer.validated_data.get('created_date')

        review = Review.objects.create(author=author, doctor=doctor, text=text, created_date=created_date)
        return Response(data=DoctorDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)