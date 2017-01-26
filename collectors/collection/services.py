from collectors.collection.models import Collection


class CollectionService(object):

    @staticmethod
    def list():
        return Collection.objects.all()