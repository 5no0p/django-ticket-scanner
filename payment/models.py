import uuid

from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from ticket.models import Ticket


PAYE_STAUTS_CHOICES = (
    ("F", "Full Paid"),
    ("N", "Not Paid"),
    ("S", "Semi Paid"),
)

class Payment(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    purchased_by = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="payment", on_delete=models.CASCADE) 
    ticket = models.OneToOneField(Ticket,related_name="payment_info", on_delete=models.CASCADE)
    amount_of_payment = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=PAYE_STAUTS_CHOICES)
    purchased_at = models.DateField(auto_now_add=True, null=True)
    screenshot = models.ImageField(upload_to ='payment/screenshots/')

    def __str__(self):
        return str(self.uuid)