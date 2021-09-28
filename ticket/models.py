import uuid

from django.db import models
from django.db.models.fields.json import JSONField
from event.models import Event
from django.conf import settings


SCAN_STAUTS_CHOICES = (
    ("P", "Pass"),
    ("E", "Expire"),
    ("I", "Issue"),
    ("N", "Null"),
)

class Category(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False,unique=True)
    name = models.CharField(max_length=150)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    discripton = models.CharField(max_length=350,null=True)
    event = models.ForeignKey(Event, related_name="ticket_categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Ticket(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False,unique=True)
    name = models.CharField(max_length=150)
    #purchased_at = models.DateField(auto_now_add=True)
    validity = models.BooleanField(default=True)
    category = models.ForeignKey(Category,related_name="tickets",null=True ,on_delete=models.CASCADE)
    #purchased_by = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="tickets", on_delete=models.CASCADE)
    extral_info = JSONField()

    def __str__(self):
        return self.name

class ScanLogs(models.Model):
    ticket = models.ForeignKey(Ticket,related_name="scan_logs", on_delete=models.CASCADE)
    scan_time = models.TimeField()
    scanned_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="tickets_scan_logs", on_delete=models.CASCADE)
    status_recorded = models.CharField(max_length=1,null=True,blank=False, choices=SCAN_STAUTS_CHOICES)

    def __str__(self):
        return self.status_recorded