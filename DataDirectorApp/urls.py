from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fileupload/', include('fileupload.urls')),
    path('admin/', admin.site.urls),
]