from rest_framework import serializers
from .models import Review, Doctor, Record


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text author doctor created_date'.split()


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = 'id image name patronymic datetime post education experience'.split()


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = 'id phone_number date service doctor'.split()