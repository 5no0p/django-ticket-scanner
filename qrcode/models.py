import uuid

from django.db import models
from django.db.models.deletion import CASCADE
from ticket.models import Ticket


class QRcodeGenerator(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=500)
    qrimage = models.ImageField(upload_to ='QRcode/')