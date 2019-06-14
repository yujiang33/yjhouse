from django.conf.urls import url
from .Feed import ArticleFeed
from .import views
app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name='single'),
    url(r'^archives/(\d+)/(\d+)/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^category/(\d+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tags/(\d+)/$',views.TagsView.as_view(),name='tags'),
    url(r'rss/$',ArticleFeed(),name="rss")
]
