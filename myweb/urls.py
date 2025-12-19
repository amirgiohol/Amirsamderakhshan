from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.profaile.urls")),
    path("contact/", include("app.contact.urls")),
    path("", home),
]

def home(request):
    return HttpResponse("OK")