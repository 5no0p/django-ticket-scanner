import uuid

from django.db import models, transaction
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from colorfield.fields import ColorField

from event.models import Event


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
         editable = False,
         unique=True)
    name = models.CharField(max_length=150)
    color = ColorField(default='#000000')
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
    tid = models.CharField(max_length=13,null=True,blank=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10,null=True,blank=True)
    validity = models.BooleanField(default=True)
    category = models.ForeignKey(Category,related_name="tickets",null=True ,on_delete=models.CASCADE)
    table = models.IntegerField(null=True,blank=True)
    qrcode = models.CharField(max_length=100,unique=True,null=True,blank=True)
    isSend = models.BooleanField(default=False)
    number = models.PositiveIntegerField(null=True,blank=True)
    is_checked = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['isSend','number']
        permissions=[
            ("change_validity_status", "Can change the validity status of ticket"),
            ("change_checked_status", "Can change the check status of the ticket")
        ]

    def __str__(self):
        return self.name

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.qrcode or not self.tid:
            import secrets
            import string
        
            chars = string.ascii_letters + string.digits
            #special_chars = '_!/?'
            length = 30
            uiLenth = 13

            if not self.qrcode:
                while True:
                    passwd = ''.join([secrets.choice(chars) for i in range(length)]) #range(length-1)
                    #passwd += secrets.choice(special_chars)
                    if (any(s.islower() for s in passwd) and 
                        any(s.isupper() for s in passwd) and 
                        any(s.isdigit() for s in passwd)):
                            break
                self.qrcode = passwd
            if not self.tid:
                uid = ''.join([secrets.choice(string.ascii_lowercase) for i in range(uiLenth-10)])
                uid += ''.join([secrets.choice(string.digits) for i in range(uiLenth-3)])
                self.tid = uid
        super(Ticket, self).save(*args, **kwargs)



class ScanLogs(models.Model):
    ticket = models.ForeignKey(Ticket,related_name="scan_logs", on_delete=models.CASCADE)
    scan_time = models.TimeField()
    scanned_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="tickets_scan_logs", on_delete=models.CASCADE)
    status_recorded = models.CharField(max_length=1,null=True,blank=False, choices=SCAN_STAUTS_CHOICES)

    def __str__(self):
        return self.status_recorded


class SecurityLayer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    layer = models.PositiveSmallIntegerField(unique=True, null=True, blank=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='security')

    class Meta:
        ordering = ['layer']

    def clean(self) -> None:
        if self.layer > (SecurityLayer.objects.all().count() + 1):
            raise ValidationError({'layer':_(F'Security layer should not be more than {SecurityLayer.objects.all().count() + 1}')})

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super(SecurityLayer, self).save(*args, **kwargs)

class TicketCheck(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='check_process', on_delete=models.CASCADE)
    security_layer = models.ForeignKey(SecurityLayer, related_name='ticket_check', on_delete=models.CASCADE)
    checked_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="ticket_check", on_delete=models.CASCADE)
    checked_at = models.TimeField(default=timezone.now)