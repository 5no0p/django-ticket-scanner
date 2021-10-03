from django.contrib import admin
from django.urls import reverse
from payment.models import Payment
from ticket.models import Ticket

class TicketInline(admin.TabularInline):
    model = Ticket
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'purchased_by', 'ticket', 'amount_of_payment', 'status', 'purchased_at']
    list_filter = ['status']
    inlines = [
        TicketInline,
    ]



admin.site.register(Payment, PaymentAdmin)