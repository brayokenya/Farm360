from django.contrib import admin
from .models import Collection, Sample


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'disease_term', 'title')

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_collection', 'user', 'donor_count', 'material_type', 'last_updated')

    def display_collection(self, obj):
        return obj.collection.title  
    display_collection.short_description = 'Collection'