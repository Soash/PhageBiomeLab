from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ongoing-research/', views.ongoing_research, name='ongoing_research'),
    path('published-research/', views.published_research, name='published_research'),
    path('members/', views.members, name='members'),
    path('gallery/', views.gallery_view, name='gallery_view'),
    path('database/', views.database_view, name='database_view'),
]
