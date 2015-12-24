from django.test import TestCase

# Create your tests here.
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
 
urlpatterns = [
    url(r'^$', views.BeerList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BeerDetail.as_view()),
]
 
urlpatterns = format_suffix_patterns(urlpatterns)