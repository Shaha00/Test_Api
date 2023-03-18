from rest_framework import serializers
from .models import Review, Doctor


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text author doctor created_date'.split()


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = 'id image name patronymic datetime post education experience'.split()