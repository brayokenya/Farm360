from django.contrib import admin
from .models import Event, Livestock, Resource


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title','start_date','end_date','description')


@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'livestock_type', 'name', 'sex', 'identification_number', 'status')


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','name', 'type', 'description', 'quantity', 'location')
    search_fields = ('name', 'type', 'location')
    list_filter = ('type', 'location')