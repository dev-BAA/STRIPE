from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^buy/(?P<buy_id>[0-9]+)/$', views.buy, name='buy'),
    re_path(r'^item/(?P<item_id>[0-9]+)/$', views.item, name='item'),
]
