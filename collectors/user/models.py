from django.contrib.auth.models import User

from collectors.utils.models import TimeStampModel
from django.db import models


class Friendship(TimeStampModel):
    creator = models.ForeignKey(User, related_name="friendship_creator_set")
    friend = models.ForeignKey(User, related_name="friend_set")

    def __str__(self):
        return '{0} - {1}'.format(self.creator, self.friend)