from django.contrib import admin

from collectors.comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
