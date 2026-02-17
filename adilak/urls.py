from django.urls import path
from . import views

urlpatterns = [
    path('generate-excel/', views.generate_excel, name='generate_excel'),
]