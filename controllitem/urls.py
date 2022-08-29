from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from controllitem.store import urls

admin.site.site_header = "Controll Item"
admin.site.site_title = "Controll Item"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Controll Item API",
            default_version='v1',
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
