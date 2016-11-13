from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^events$', views.events, name="events"),
    url(r'^terminal', views.termninal, name="terminal")
]
