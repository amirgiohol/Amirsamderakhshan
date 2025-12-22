from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ویوی تستی
def health_check(request):
    return HttpResponse("✅ سایت کار میکند!", content_type="text/plain; charset=utf-8")
def health(request):
    return HttpResponse("OK")

urlpatterns = [
    path('', health),                
    path("admin/", admin.site.urls),
    path("test/", health_check),  # اول این خط رو اضافه کن
    path("", include("app.profaile.urls")),
    path("contact/", include("app.contact.urls")),
    
    
]