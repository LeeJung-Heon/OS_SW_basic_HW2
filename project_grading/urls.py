from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("grading.urls")),
    path('admin/', admin.site.urls),
]
