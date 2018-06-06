from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^product/(?P<product_id>[0-9]+)/', views.product_detail, name='product_detail'),
    re_path(r'^charge/$', views.charge, name='charge'),
]