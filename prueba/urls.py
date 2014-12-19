from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from load_data.api import StockResource

v1_api = Api(api_name='v1')
v1_api.register(StockResource())




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^load_data/', include('load_data.urls')),
)
