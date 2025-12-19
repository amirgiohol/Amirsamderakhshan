from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # یا هر ویوی دیگری که داری
]