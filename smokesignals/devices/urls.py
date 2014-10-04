# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from devices import views

urlpatterns = patterns('',
    # URL pattern for the DeviceListView  # noqa
    url(
        regex=r'^$',
        view=views.DeviceListView.as_view(),
        name='list'
    ),
    # # URL pattern for the UserRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),
    # URL pattern for the DeviceDetailView
    url(
        regex=r'^(?P<pk>[\d]+)/$',
        view=views.DeviceDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the DeviceUpdateView
    url(
        regex=r'^update/(?P<pk>[\d]+)/$',
        view=views.DeviceUpdateView.as_view(),
        name='update'
    ),
    # URL pattern for the DeviceDeleteView
    url(
        regex=r'^delete/(?P<pk>[\d]+)/$',
        view=views.DeviceDeleteView.as_view(),
        name='delete'
    ),
    url(
        regex=r'^create/$',
        view=views.DeviceCreateView.as_view(),
        name='create'
    ),
)
