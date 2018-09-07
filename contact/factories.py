import factory

from django.contrib.auth.models import User

from contact.models import Contact


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = factory.Sequence(lambda x: "user{}".format(x))


class ContactFactory(factory.DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    profil_picture = factory.django.ImageField(color='blue')
    added_by = factory.SubFactory(UserFactory)
