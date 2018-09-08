from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from contact.factories import ContactFactory
from event.factories import EventFactory

# Create your tests here.


class DashboardOverviewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )
        cls.contact = ContactFactory(
            added_by=cls.admin,
        )

        cls.event = EventFactory(
            contact=cls.contact,
            user = cls.admin,
        )

    def setUp(self):
        self.client.login(username=self.admin.username, password="test1234")

    def test_access_to_dashboard(self):
        result = self.client.get(
            reverse("dashboard"),
            follow=True

        )
        self.assertEqual(result.status_code, 200)
