from django.conf.urls import url
from event.views import CreateEvent, UpdateEvent, DeleteEvent

urlpatterns = [
    url(r'^new', CreateEvent.as_view(), name='create_event'),
    url(r'^update/(?P<pk>\d+)', UpdateEvent.as_view(), name='update_event'),
    url(r'^delete/(?P<pk>\d+)', DeleteEvent.as_view(), name='delete_event')
]