from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("OK")

urlpatterns = [
    path("", home),
]
