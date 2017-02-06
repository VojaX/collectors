from django.contrib import admin

from collectors.user.models import Friendship


class FriendshipAdmin(admin.ModelAdmin):
    pass

admin.site.register(Friendship, FriendshipAdmin)