from django.urls import path
from . import views
from .views import profilesAPI, projectsAPI,home,projects

urlpatterns=[
    path('api/profiles',profilesAPI.as_view(),name='profiles_api'),
    path('api/profiles/id=<int:id>',profilesAPI.as_view(),name='profiles_api_by_id'),
    path('api/profiles/username=<str:username>',profilesAPI.as_view(),name='profiles_api_by_username'),
    path('api/projects/username=<str:username>',projectsAPI.as_view(),name='projects_api_by_username'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('<str:username>',projects.as_view(),name='projects'),
    path('',home.as_view(),name='home')
]