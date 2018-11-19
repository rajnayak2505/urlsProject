from django.shortcuts import render
from django.http import HttpResponse

def hydJobsInfo(request):
    s="<h1>Hydrabad jobs information</h1>"
    return HttpResponse(s)

def mumJobsInfo(request):
    s="<h1>Mumbai jobs information</h1>"
    return HttpResponse(s)

def puneJobsInfo(request):
        s="<h1>Pune jobs information</h1>"
        return HttpResponse(s)

def noidaJobsInfo(request):
    s="<h1>Noida jobs information</h1>"
    return HttpResponse(s)
