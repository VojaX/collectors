from django.contrib.auth.models import User
from django.db import models

from collectors.collection.models import Collection
from collectors.utils.models import TimeStampModel


class Comment(TimeStampModel):
    body = models.TextField()
    owner = models.ForeignKey(User, related_name='owner')
    collection = models.ForeignKey(Collection, related_name='collection',
                                   null=True)

    def __str__(self):
        return self.body