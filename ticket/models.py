import uuid

from django.db import models, transaction
from colorfield.fields import ColorField
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
    table = models.IntegerField(null=True)
    qrcode = models.CharField(max_length=100,unique=True,null=True,blank=True)


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