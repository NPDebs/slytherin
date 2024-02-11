from django.urls import path
from . import views

urlpatterns = [
    path('gpa_calculator/', views.gpa_calculator, name='gpa_calculator'),
]