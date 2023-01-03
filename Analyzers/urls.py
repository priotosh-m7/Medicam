from django.urls import path
from django.contrib import admin
from django.urls import path, include
from  . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'polls'
urlpatterns = [
    path('brain', views.brainTumor, name='bt'),
    path('chest', views.chestXray, name='cx'),
    path('kidney', views.kidneyScans, name='ks'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)