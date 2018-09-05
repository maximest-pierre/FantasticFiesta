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
