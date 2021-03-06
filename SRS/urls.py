"""SRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup$', views.index, name = 'index'),
    url(r'^$', views.index, name='index'),
    url(r'^JobOpenings$', views.myview_job, name='jobopening'),
    url(r'^Status$', views.myview_status, name='status'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^savedata$', views.savedata, name = 'savedata'),
    url(r'^uploadaadhaar$', views.savedata, name = 'savedata'),
    url(r'^applicantdetails$', views.applicant_details, name = 'applicant_details'),

    path('apply/<int:ID>/', views.apply_to_job),
    #url(r'^.*$', views.index, name = 'index'),
]