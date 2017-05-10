from django.conf.urls import url
from hp.views import ProductLV,ProductDV

urlpatterns = [
    url(r'^product/$', ProductLV.as_view(), name='index'),
    url(r'^product/(?P<pk>\d+)$', ProductDV.as_view(), name='detail'),
]
