from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'experience_years', 'email', 'phone', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']