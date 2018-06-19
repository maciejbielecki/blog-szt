from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^category/(?P<category>.+)$', views.post_list_category, name='post_list_category'),
    url(r'^author/(?P<author>.+)$', views.post_list_author, name='post_list_author'),
    url(r'^search$', views.post_list_search, name='post_list_search'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^kontakt$', views.contact, name='contact'),
    url(r'^post/new/$', views.post_new, name='post_new'),    
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^login$', views.user_login, name='user_login'),
	url(r'^register$', views.user_register, name='user_register'),
	url(r'^logout/(?P<user>[0-9]+)$', views.user_logout, name='user_logout'),
	url(r'^delete/(?P<pk>[0-9]+)$', views.post_delete, name='post_delete'),
	url(r'^publish/(?P<pk>[0-9]+)$', views.post_publish, name='post_publish'),
	url(r'^post_all$', views.post_all, name='post_all'),
	url(r'^post_unpublish', views.post_unpublish, name='post_unpublish'),
]