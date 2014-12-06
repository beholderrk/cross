from django.conf.urls import patterns, include, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^stat/post/$', 'post_stat', name='post_stat'),
    url(r'^stat/get/$', 'get_stat', name='get_stat'),
)
