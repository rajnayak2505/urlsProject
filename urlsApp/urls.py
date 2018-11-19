from django.conf.urls import url
from urlsApp import views

urlpatterns = [
    url(r'^hydjobs/', views.hydJobsInfo),
    url(r'^mumjobs/', views.mumJobsInfo),
    url(r'^punjobs/', views.puneJobsInfo),
    url(r'^noijobs/', views.noidaJobsInfo),
]
