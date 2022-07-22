from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    exclude = ['eid']
    list_display = ['eid', 'name']
    ordering = ['active_in']


admin.site.register(Event, EventAdmin)