from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Doctor assigned to patient successfully',
                'mapping': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MappingByPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response({'message': 'Mapping removed successfully'}, status=status.HTTP_200_OK)