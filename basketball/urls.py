from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^index$',views.index),
    url(r'^home$',views.home),
    url(r'^teams$',views.teams),
    url(r'^schedule$',views.schedule),
    url(r'^credit$',views.credit),
    url(r'^playoff$',views.playoff),
    url(r'^update_credit$',views.update_credit),
    url(r'^update_playoff$', views.update_playoff),
]