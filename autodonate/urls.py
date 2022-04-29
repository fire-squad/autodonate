"""``autodonate`` URL Configuration.

The ``urlpatterns`` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from decouple import config

from autodonate.settings import DEBUG

urlpatterns = [
    path("", include("index.urls")),
    path("api/", include("api.urls")),
    path(config("DJANGO_ADMIN_URL", default="django-admin/"), admin.site.urls),
]

if DEBUG:
    # Stub for debug_toolbar
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    
    # Serve user-uploaded media files for debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    admin.site.site_title = "autodonate"
    admin.site.site_header = "Admin panel"
    admin.site.index_title = "autodonate"
