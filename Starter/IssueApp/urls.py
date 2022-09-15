from django.urls import re_path
from IssueApp import views


urlpatterns=[
re_path(r'^issue$', views.Issues.as_view(), name ='issue'),
re_path(r'^issue/$', views.IssuesbyId.as_view(),name='id'),
re_path('issue/search/', views.Issuesbytitle.as_view(),name='title'),
]