from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from utils.mixins import IdentifierLookupMixin

class AppointmentUserViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=False, methods=['get'])
    def patient_appointments(self, request, *args, **kwargs):
        patient_id = request.query_params.get('patientid')
        if not patient_id:
            return Response({'detail': 'Patient ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.queryset.filter(patient_id=patient_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def doctor_appointments(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctorid')
        if not doctor_id:
            return Response({'detail': 'Doctor ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.queryset.filter(doctor_id=doctor_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DoctorAppointmentsList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    def get_queryset(self):
        doctor_id = self.kwargs['doctor_id']
        return self.queryset.filter(doctor_id=doctor_id)
    
class PatientAppointmentsList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return self.queryset.filter(patient_id=patient_id)
    

class DoctorAppointmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class PatientAppointmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer