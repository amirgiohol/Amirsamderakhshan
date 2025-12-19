from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("OK")


urlpatterns = [
    path("", home),  # Healthcheck قطعی
    path("admin/", admin.site.urls),
    path("profile/", include("app.profaile.urls")),
    path("contact/", include("app.contact.urls")),
]
