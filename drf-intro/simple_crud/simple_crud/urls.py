"""simple_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from measurements import views

router1 = DefaultRouter()
router1.register('api/v1/project', views.ProjectViewSet, basename='projects')

router2 = DefaultRouter()
router2.register('api/v1/measurement', views.MeasurementViewSet, basename='measurements')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router1.urls), name='projects'),
    path('', include(router2.urls), name='measurements')
    ]
