import uuid

from django.db import models
from django.db.models.fields.json import JSONField
from event.models import Event
from django.conf import settings


class Category(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=150)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    discripton = models.CharField(max_length=350)
    event = models.ForeignKey(Event, related_name="ticket_categories", on_delete=models.CASCADE)
    

class Ticket(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=150)
    purchased_at = models.DateField(auto_now_add=True)
    validity = models.BooleanField()
    purchased_by = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="tickets", on_delete=models.CASCADE)
    extral_info = JSONField()

class ScanLogs(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    scan_time = models.TimeField()
    scanned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)