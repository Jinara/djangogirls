from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'(?P<param>[0-9]+)/$', views.myfirstview, name='myfirstview')
]
