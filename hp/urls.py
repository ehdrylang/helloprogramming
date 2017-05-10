from django.conf.urls import url
from hp.views import ProductLV,ProductDV

urlpatterns = [
    url(r'^$', ProductLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', ProductDV.as_view(), name='detail'),
]
