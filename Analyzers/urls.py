from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('brain', views.brainTumor, name='bt'),
    path('chest', views.chestXray, name='cx'),
    path('kidney', views.kidneyScans, name='ks'),
]