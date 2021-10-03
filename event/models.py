import uuid
from psycopg2.extras import DateTimeTZRange
from django.utils import timezone
from datetime import timedelta

from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import DateTimeRangeField
from django.conf import settings

def default_active_in():
    now = timezone.now()
    return DateTimeTZRange(now + timedelta(days=2), now + timedelta(days=5))

class Event(models.Model):
    uuid = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False,unique=True)
    name = models.CharField(max_length=200)
    #slug = models.SlugField(max_length=250,null=True,blank=True)
    discripton = models.CharField(max_length=350)
    active_in = DateTimeRangeField(default=default_active_in) 
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="owned_events", on_delete=models.CASCADE)

    def __str__(self):
        return self.name