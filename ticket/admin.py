from django.contrib import admin
from ticket.models import Ticket,Category,ScanLogs

class TicketAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ScanLogsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScanLogs, ScanLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)