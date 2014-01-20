try:
	from django.conf.urls import patterns, include, url
except ImportError:
	from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView

from .views import SwaggerView, ResourcesView, SchemaView

urlpatterns = patterns('',
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources$', ResourcesView.as_view(), name='resources'),
    url(r'^resources/(?P<resource>\S+)$', SchemaView.as_view()),
    url(r'^resources$', SchemaView.as_view(), name='schema'),
    url(r'^images/throbber\.gif', RedirectView.as_view(url='%stastypie_swagger/images/throbber.gif' % settings.STATIC_URL)),
)
