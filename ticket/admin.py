from django.contrib import admin
from ticket.models import Ticket,Category,ScanLogs
from ticket.actions import make_valid

from payment.models import Payment

class PaymentInline(admin.TabularInline):
    model = Payment
class TicketAdmin(admin.ModelAdmin):
    exclude = ('qrcode',)
    list_display = ['uuid', 'name', 'validity', 'category', 'table']
    ordering = ['category']
    list_filter = ['category',["qrcode", admin.EmptyFieldListFilter]]
    search_fields = ['qrcode']
    actions = [make_valid]
    inlines = [
        PaymentInline,
    ]
        
class CategoryAdmin(admin.ModelAdmin):
    pass

class ScanLogsAdmin(admin.ModelAdmin):
    list_display = ['get_ticket', 'scan_time', 'status_recorded', 'get_event', 'scanned_by']
    ordering = ['-scan_time']
    list_filter = ['status_recorded','scanned_by', 'ticket__category__event__name']

    @admin.display(ordering='ticket__uuid', description='Ticket')
    def get_ticket(self, obj):
        return obj.ticket.uuid

    @admin.display(ordering='ticket__category__event__name', description='Event')
    def get_event(self, obj):
        return obj.ticket.category.event.name


admin.site.register(ScanLogs, ScanLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)