from django.contrib import admin

from collectors.collection.models import Collection, CollectionType, CollectionSubType, Category


class CollectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionType, CollectionAdmin)
admin.site.register(CollectionSubType, CollectionAdmin)
admin.site.register(Category, CollectionAdmin)
 
