from django.conf.urls import patterns, include, url
from events import views

urlpatterns = [
    url(r'^events/$', views.events, {"template":"main/events.html"}),
    url(r'^events/(?P<pk>\w+)/rsvp/$', views.rsvp, name="rsvp_event"),
    url(r'^events/(?P<pk>\w+)/rsvp/remove$', views.un_rsvp, name="rm_rsvp_event"),
]