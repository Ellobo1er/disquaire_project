"""disquaire_project URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views # import views so we can use them in urls.

urlpatterns = [
    url(r'^$', views.listing, name="listing"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^search/$', views.search, name="search"),
   
]
app_name='store'

#urlpatterns = [
   
    #url(r'^$', views.listing),
   # url(r'^(?P<album_id>[0-9]+)/$', views.detail),
#]