from django.contrib import admin
from ticket.models import Ticket,Category,ScanLogs
from ticket.actions import make_valid
class TicketAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'validity', 'category', 'table']
    ordering = ['category']
    actions = [make_valid]

class CategoryAdmin(admin.ModelAdmin):
    pass

class ScanLogsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScanLogs, ScanLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)