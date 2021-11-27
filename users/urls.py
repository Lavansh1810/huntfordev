from django.urls import path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profiles, name='profiles'),
    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('add-skill/', views.addSkill, name='add-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),


    url(r'^media/(?P<path>.*)$', serve,{'document_root': 
          settings.MEDIA_ROOT}),       
    url(r'^static/(?P<path>.*)$', serve,{'document_root': 
    settings.STATIC_ROOT}), 
]