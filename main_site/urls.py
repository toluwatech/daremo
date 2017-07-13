# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views # import from the current package


# Create your views here.
urlpatterns = [
  url(r'^$', views.index, name='index'), # the url starts and ends - '^$' - so its index
	url(r'^contact/$', views.contact, name='contact'),

  ] 