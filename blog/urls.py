from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'blog/^$', views.blog, namespace='blog'),
]
