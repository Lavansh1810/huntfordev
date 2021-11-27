from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create_project/', views.create_project, name="create_project"),
    path('update_project/<str:pk>/', views.update_project, name="update_project"),
    path('delete_project/<str:pk>/', views.delete_project, name="delete_project"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root': 
          settings.MEDIA_ROOT}),       
    url(r'^static/(?P<path>.*)$', serve,{'document_root': 
    settings.STATIC_ROOT}), 
    
]
