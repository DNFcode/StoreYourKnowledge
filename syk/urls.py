"""syk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from .views import HomePageRedirectView

urlpatterns = [
    url(r'^$', HomePageRedirectView.as_view(), name='index'),
    url(r'^welcome/$', TemplateView.as_view(template_name="index.html"), name="welcome"),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('syk.apps.users.urls')),
    url(r'^app/', include('syk.apps.main.urls')),

    # override signup view and url for allauth
    url(r'^accounts/social/signup/$', TemplateView.as_view(template_name="email_exists.html"), name='socialaccount_signup'),
    url(r'^accounts/', include('allauth.urls')),
]
