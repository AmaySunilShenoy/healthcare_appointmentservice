from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListCreate.as_view(), name='appointment-createlist'),
    path('<int:pk>/', views.AppointmentRetrieveUpdateDestroy.as_view(), name='appointment-manage'),
]