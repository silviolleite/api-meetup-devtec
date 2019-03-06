"""meetup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from meetup.api.urls import router
from meetup.core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
    # path('inscricao/', include('meetup.subscriptions.urls')),
    # path('palestrantes/<slug:slug>/', speaker_detail, name='speaker_detail'),
    # path('palestras/', talk_list, name='talk_list'),
    path('admin/', admin.site.urls),
]
