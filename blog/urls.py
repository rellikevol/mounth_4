from django.urls import path
from blog import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name='index-page'),
    path('contacts/', views.get_contacts, name='contacts_page'),
    path('about/', views.get_about, name='about_page'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>', views.post_delete, name='post-delete'),
    path("post/create", views.PostCreateView.as_view(), name='post-create'),
    path('post/delete/accept/<int:pk>', views.PostDeleteView.as_view(), name='post-delete-accept'),
]