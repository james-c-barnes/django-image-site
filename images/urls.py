from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.ImageList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/data/$', views.ImageData.as_view()),
]
