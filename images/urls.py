from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.ServiceImageList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.ServiceImageDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/data$', views.ServiceImageData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
