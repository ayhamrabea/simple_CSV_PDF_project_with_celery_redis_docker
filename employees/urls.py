from django.urls import path
from .views import EmployView , EmploytListView , generate_csv , generate_pdf

urlpatterns = [
    path('',EmploytListView.as_view(),name='home'),
    path('add',EmployView.as_view(),name='add_employ'),

    path('generate-csv/', generate_csv, name='generate_csv'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
]
