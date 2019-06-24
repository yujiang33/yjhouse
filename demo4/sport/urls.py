from django.conf.urls import url
from sport.views import *
from haystack.views import SearchView
app_name = 'sport'
urlpatterns =[
    url(r'^$', IndexView.as_view(),name='index'),
    url(r'^blog/$',BlogView.as_view(),name='blog'),
    url(r'^single/(\d+)/$',SingleView.as_view(),name='single'),
    url(r'^category/(\d+)/$',CategoryView.as_view(),name="category"),
    url(r'^archieves/(\d+)/(\d+)/$',ArchievesView.as_view(),name="archieves"),
    url(r'^search/$',SearchView(),name='search'),
    url(r'^contact/$',ContactView.as_view(),name='contact'),
]