from django.conf.urls import patterns, url

from django.views.generic import TemplateView
from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),

)