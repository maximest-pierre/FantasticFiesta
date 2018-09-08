from django.conf.urls import url
from contact.views import CreateContact, ListContact, DetailContact, DeleteContact, UpdateContact

urlpatterns = [
    url(r'^new', CreateContact.as_view(), name='create_contact'),
    url(r'^$', ListContact.as_view(), name='list_contact'),
    url(r'^detail/(?P<pk>\d+)', DetailContact.as_view(), name='detail_contact'),
    url(r'^delete/(?P<pk>\d+)', DeleteContact.as_view(), name='delete_contact'),
    url(r'^update/(?P<pk>\d+)', UpdateContact.as_view(), name='update_contact'),
]