# Generated by Django 3.2.7 on 2021-09-23 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='purchased_by',
        ),
    ]