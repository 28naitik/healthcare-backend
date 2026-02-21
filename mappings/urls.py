from django.urls import path
from .views import MappingListCreateView, MappingByPatientView, MappingDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('delete/<int:id>/', MappingDeleteView.as_view(), name='mapping-delete'),
]