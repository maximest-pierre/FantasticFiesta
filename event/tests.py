import datetime

from django.test import TestCase

from event.factories import EventFactory
from contact.factories import ContactFactory, UserFactory


class TestEvent(TestCase):
    @classmethod
    def setUp(cls):

        cls.time = datetime.datetime.now()

        cls.user = UserFactory()

        cls.contact = ContactFactory(
            added_by=cls.user
        )

        cls.event_status_planned = EventFactory(
            status='P',
            note='test',
            date=cls.time,
            contact=cls.contact
        )
        cls.event_status_ongoing = EventFactory(
            status='O',
            note='test',
            date=cls.time,
            contact=cls.contact
        )
        cls.event_status_completed = EventFactory(
            status='C',
            note='test',
            date=cls.time,
            contact=cls.contact
        )

    def test_planned_status(self):
        self.assertEqual(self.event_status_planned.status, 'P')

    def test_ongoing_status(self):
        self.assertEqual(self.event_status_ongoing.status, 'O')

    def test_completed_status(self):
        self.assertEqual(self.event_status_completed.status, 'C')

    def test_note(self):
        self.assertEqual(self.event_status_planned.note, 'test')

    def test_date(self):
        self.assertEqual(self.event_status_planned.date, self.time)
