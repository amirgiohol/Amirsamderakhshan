from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.profaile.urls")),
    path("contact/", include("app.contact.urls")),
]
