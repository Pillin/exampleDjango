from django.conf.urls import patterns, url

from load_data import views


METHOD_DISPATCHER = 'load_data.views.method_dispatcher'



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^csv/$',METHOD_DISPATCHER, {'GET':views.load_csv, 'POST':views.load_csv_post}, name='load_csv'),
)