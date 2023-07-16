from django.contrib import admin
from django.urls import path, include
from daily_location.views import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]