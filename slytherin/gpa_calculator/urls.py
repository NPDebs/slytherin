from django.urls import path
from . import views

urlpatterns = [
    # Map the URL 'gpa_calculator/' to the 'gpa_form' view
    path('gpa_calculator/', views.gpa_form, name='gpa_form'),
    
    # Map the URL 'gpa_calculator/calculate' to the 'gpa_calculator' view
    path('gpa_calculator/calculate/', views.gpa_calculator, name='gpa_calculator'),
]
