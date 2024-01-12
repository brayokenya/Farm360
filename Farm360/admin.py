from django.contrib import admin
from .models import Event, Livestock


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title','start_date','end_date','description')


@admin.register(Livestock)
class LivestockAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'livestock_type', 'name', 'sex', 'identification_number', 'status')
