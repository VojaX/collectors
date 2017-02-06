from django.contrib.auth.models import User
from faker import Factory as FakerFactory
import factory

from collectors.collection.factories import CollectionFactory
from collectors.comments.models import Comment

faker = FakerFactory.create('en')


class CommentFactory(factory.DjangoModelFactory):
    body = factory.LazyAttribute(lambda n: faker.sentence())
    collection = factory.SubFactory(CollectionFactory)
    owner = User.objects.first()

    class Meta:
        model = Comment