from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase

from contact.factories import ContactFactory, UserFactory


class ContactTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.user = UserFactory()
        cls.contact = ContactFactory(
            first_name="test",
            last_name="test",
            email="test@example.com",
            added_by=cls.user
        )

    def test_contact_first_name(self):
        self.assertEqual(self.contact.first_name, "test")

    def test_contact_last_name(self):
        self.assertEqual(self.contact.last_name, "test")

    def test_contact_email(self):
        self.assertEqual(self.contact.email, "test@example.com")

    def test_user(self):
        self.assertEqual(self.contact.added_by.username, self.user.username)


class ListContactTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_superuser(
            username="admin@example.com",
            email="admin@example.com",
            password="test1234"
        )
        cls.contact = ContactFactory(
            first_name="test",
            last_name="test",
            email="test@example.com",
            added_by=cls.user
        )

    def setUp(self):
        self.client.login(username=self.user.username, password="test1234")


    def test_access_list_contact(self):
        result = self.client.get(
            reverse("contact:list_contact"),
            follow=True

        )
        self.assertEqual(result.status_code, 200)