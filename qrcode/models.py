import uuid

from django.db import models
from django.db.models.deletion import CASCADE
from ticket.models import Ticket


class QrcodeGenerator(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False,unique=True)
    ticket = models.ForeignKey(Ticket,related_name='ticket_qrcode', on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=500,unique=True,null=True,blank=True)
    #qrimage = models.ImageField(upload_to ='QRcode/', null=True, blank=True)

    def __str__(self):
         return self.qrcode