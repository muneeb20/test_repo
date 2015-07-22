from django.conf.urls import patterns, url
from views import SortStringListView

urlpatterns = patterns('',
                       url(r'^sort_string_list/?$', SortStringListView.as_view(), name='string_list'),
                       )