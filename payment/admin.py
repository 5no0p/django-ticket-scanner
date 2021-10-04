from django.contrib import admin
from django.urls import reverse
from payment.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'purchased_by', 'ticket', 'amount_of_payment', 'status', 'purchased_at']
    list_filter = ['status']


admin.site.register(Payment, PaymentAdmin)