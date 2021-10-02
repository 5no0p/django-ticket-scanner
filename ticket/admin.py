from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from ticket.models import Ticket,Category,ScanLogs
from ticket.actions import make_valid
class TicketAdmin(admin.ModelAdmin):
    exclude = ('qrcode',)
    list_display = ['uuid', 'name', 'validity', 'category', 'table']
    ordering = ['category']
    actions = [make_valid]

    def make_valid(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d ticket was successfully marked as valid.',
            '%d tickets were successfully marked as valid.',
            updated,
        ) % updated, messages.SUCCESS)

class CategoryAdmin(admin.ModelAdmin):
    pass

class ScanLogsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScanLogs, ScanLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)