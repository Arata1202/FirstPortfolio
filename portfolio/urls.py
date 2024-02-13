from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import frontpage, traveljapansite, portfoliosite

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage),
    path("traveljapansite/",traveljapansite),
    path("portfoliosite/",portfoliosite),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
