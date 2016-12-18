from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.ImageList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.ImageDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/data$', views.ImageData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
