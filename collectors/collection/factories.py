from cities_light.models import Country
from faker import Factory as FakerFactory
import factory
import factory.fuzzy
from collectors.collection.models import Category, Collection, CollectionSubType, CollectionType, Set

faker = FakerFactory.create('en')


class SetFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda n: faker.sentence())

    class Meta:
        model = Set


class CollectionSubTypeFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda n: faker.sentence())
    set = factory.SubFactory(SetFactory)

    class Meta:
        model = CollectionSubType


class CollectionTypeFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda n: faker.sentence())
    subtype = factory.SubFactory(CollectionSubTypeFactory)

    class Meta:
        model = CollectionType


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda n: faker.sentence())
    type = factory.SubFactory(CollectionTypeFactory)

    class Meta:
        model = Category


class CollectionFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda n: faker.sentence())
    category = factory.SubFactory(CategoryFactory)
    description = factory.LazyAttribute(lambda n: faker.sentence())
    Count = factory.fuzzy.FuzzyInteger(1, 150)
    views_no = factory.fuzzy.FuzzyInteger(1, 150)
    user_possession = factory.fuzzy.FuzzyInteger(1, 150)
    likes = factory.fuzzy.FuzzyInteger(1, 150)
    country = factory.fuzzy.FuzzyChoice(Country.objects.all())
    publicated = factory.LazyAttribute(
        lambda n: faker.date_time_between()
    )
    numeration = factory.LazyAttribute(lambda n: faker.sentence())
    reverse_photo = 'https://unsplash.it/200/300/?random'
    obverse_photo = 'https://unsplash.it/200/300/?random'

    class Meta:
        model = Collection
