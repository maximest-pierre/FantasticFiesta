import datetime
import factory

from contact.factories import ContactFactory, UserFactory
from event.models import Event


class EventFactory(factory.DjangoModelFactory):
    class Meta:
        model = Event

    contact = factory.RelatedFactory(ContactFactory)
    status = 'P'
    note = 'test'
    date = datetime.datetime.now()
    user = UserFactory()
