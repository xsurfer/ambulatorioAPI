"""ambulatorio URL Configuration

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
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^pazienti/(?P<pk>[0-9]+)/visite/$', views.VisitaList.as_view(), name='visite-list'),
    url(r'^visite/(?P<paziente_pk>[0-9]+)/(?P<pk>[0-9]+)/$', views.VisitaDetail.as_view(),
        name='visite-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
