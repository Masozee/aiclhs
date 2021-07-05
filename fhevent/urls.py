
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

admin.sites.AdminSite.site_header = 'AICLHS UNIKA ATMA JAYA'
admin.sites.AdminSite.site_title = 'AICLHS UNIKA ATMA JAYA'
admin.sites.AdminSite.index_title = 'AICLHS UNIKA ATMA JAYA'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.url')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)