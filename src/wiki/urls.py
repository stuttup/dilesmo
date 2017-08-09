from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^query/$', views.query_page, name='query'),
    url(r'^results/$', views.results_page, name='results'),
]