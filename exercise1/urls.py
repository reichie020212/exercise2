from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^printed/(?P<pk>\d+)/$', views.printed, name="printed"),
    url(r'', views.print_exercise1,name="exercise1"),
]