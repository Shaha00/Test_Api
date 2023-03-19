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


class DoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = 'id image name patronymic datetime post education experience doctor_reviews'.split()



class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = 'id phone_number date service doctor'.split()


class DoctorValidateSerializer(serializers.Serializer):
    image = serializers.ImageField(default='photo_2023-03-18_20-43-19.jpg')
    name = serializers.CharField()
    patronymic = serializers.CharField()
    datetime = serializers.DateField()
    post = serializers.CharField()
    education = serializers.CharField()
    experience = serializers.IntegerField()