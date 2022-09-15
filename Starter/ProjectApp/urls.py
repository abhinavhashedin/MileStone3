from django.urls import re_path
from ProjectApp import views


urlpatterns=[
re_path(r'^project$' ,views.Projects.as_view(), name='project'),
re_path('project/delete/',views.ProjectsDeletebyId.as_view()),
re_path('project/search/', views.ProjectsbyIdParam.as_view()),
]