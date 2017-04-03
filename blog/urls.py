from django.conf.urls import url

from . import views

app_name='blog'

urlpatterns = [
	url(r'^login/$', views.loginto, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^process/$', views.process, name='process'),
	url(r'^logindone/$', views.logindone, name='logindone'),
	url(r'^(?P<user_id>[0-9]+)/feed/$', views.feed, name='feed'),
	url(r'^(?P<user_id>[0-9]+)/profile/$', views.profile, name='profile'),
	url(r'^logout/$', views.logouto, name='logout'),
	url(r'^(?P<user_id>[0-9]+)/save/$', views.savepost, name='savepost'),
	url(r'^(?P<user_id>[0-9]+)/addpost/$', views.addpost, name='addpost'),
	url(r'^(?P<user_id>[0-9]+)/(?P<post_id>[0-9]+)/deletepost/$', views.deletepost, name='deletepost'),		
]