from django.contrib.auth.models import User
from faker import Factory as FakerFactory
import factory

from collectors.user.models import Friendship

faker = FakerFactory.create('en')


class UserFactory(factory.DjangoModelFactory):
    email = factory.LazyAttribute(lambda n: faker.email())
    password = factory.PostGenerationMethodCall('set_password', 'test123')
    username = factory.LazyAttribute(lambda n: faker.email())

    class Meta:
        model = User


class FriendshipFactory(factory.DjangoModelFactory):
    creator = factory.SubFactory(UserFactory)
    friend = factory.SubFactory(UserFactory)

    class Meta:
        model = Friendship