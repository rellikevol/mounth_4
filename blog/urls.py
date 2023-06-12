from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('test-page/', views.test_page, name='test_page'),
    path('contacts/', views.get_contacts, name='contacts_page'),
    path('about/', views.get_about, name='about_page')
]