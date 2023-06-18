from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index-page'),
    path('contacts/', views.get_contacts, name='contacts_page'),
    path('about/', views.get_about, name='about_page'),
    path('post/<int:pk>', views.get_post_detail, name='post-detail'),
    path('post/update/<int:pk>', views.post_update, name='post-update'),
    path('post/delete/<int:pk>', views.post_delete, name='post-delete')
]