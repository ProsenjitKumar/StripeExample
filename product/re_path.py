from django.conf.urls import re_path
from .views import SubscribeView, SuccessView


urlpatterns = [
    re_path(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    re_path(r'^thank_you/$', SuccessView.as_view(), name='thank_you'),
]