from django.urls import path
from examples import views

urlpatterns = [
    path('template/', views.get_template, name='test_template')
]