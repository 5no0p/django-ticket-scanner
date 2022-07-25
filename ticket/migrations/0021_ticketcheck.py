# Generated by Django 3.2.9 on 2022-07-23 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0020_alter_securitylayer_layer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_at', models.TimeField(default=django.utils.timezone.now)),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_check', to=settings.AUTH_USER_MODEL)),
                ('security_layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_check', to='ticket.securitylayer')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_process', to='ticket.ticket')),
            ],
        ),
    ]
